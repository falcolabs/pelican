import { Injectable } from '@nestjs/common';
import { DatabaseService } from 'src/database/database.service';

@Injectable()
export class YearsService {
	constructor(private readonly databaseService: DatabaseService) {}

	async getYears(offset: number, limit: number) {
		return await this.databaseService.year.findMany({
			orderBy: {
				id: 'desc',
			},
			skip: offset,
			take: limit,
			select: {
				id: true,
				stage: true,
			},
		});
	}
}
