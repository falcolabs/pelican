import { Injectable } from '@nestjs/common';
import { DatabaseService } from 'src/database/database.service';

@Injectable()
export class ExamineesService {
	constructor(private readonly databaseService: DatabaseService) {}

	async getExamineesByGeneralSchool(
		yearId: string,
		generalSchoolId: string,
		offset: number,
		limit: number,
	) {
		return this.databaseService.examinee.findMany({
			where: {
				yearId,
				generalSchoolId,
			},
			select: {
				id: true,
				name: true,
				gender: true,
				birthDate: true,
				birthPlace: true,
				oldClass: true,
				oldSchool: true,
				generalSchool: {
					select: {
						name: true,
					},
				},
				priorityPoint: true,
				bonusPoint: true,
				literaturePoint: true,
				englishWPoint: true,
				englishMCPoint: true,
				mathWPoint: true,
				mathMCPoint: true,
			},
			skip: offset,
			take: limit,
		});
	}

	async getExamineesBySpecializedMajor(
		yearId: string,
		specializedSchoolId: string,
		majorId: string,
		offset: number,
		limit: number,
	) {
		return this.databaseService.examinee.findMany({
			where: {
				yearId,
				specializedSchoolId,
				majorId,
			},
			select: {
				id: true,
				name: true,
				gender: true,
				birthDate: true,
				birthPlace: true,
				oldClass: true,
				oldSchool: true,
				generalSchool: {
					select: {
						name: true,
					},
				},
				priorityPoint: true,
				bonusPoint: true,
				literaturePoint: true,
				englishWPoint: true,
				englishMCPoint: true,
				mathWPoint: true,
				mathMCPoint: true,
				specializedSchool: {
					select: {
						name: true,
					},
				},
				major: {
					select: {
						name: true,
					},
				},
				majorPoint: true,
			},
			skip: offset,
			take: limit,
		});
	}
}
