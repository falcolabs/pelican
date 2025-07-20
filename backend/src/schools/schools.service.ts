import { Injectable } from '@nestjs/common';
import { DatabaseService } from 'src/database/database.service';

@Injectable()
export class SchoolsService {
  constructor(private readonly databaseService: DatabaseService) {}

  async getSchoolsData(yearId: string) {
    return await this.databaseService.school.findMany({
      where: {
        yearId,
      },
      select: {
        id: true,
        name: true,
        logoUrl: true,
        schoolType: true,
      },
    });
  }

  async getSchoolData(yearId: string, id: string) {
    return await this.databaseService.school.findUnique({
      where: {
        yearId_id: {
          yearId,
          id,
        },
      },
      select: {
        name: true,
        logoUrl: true,
        schoolType: true,
      },
    });
  }
}
