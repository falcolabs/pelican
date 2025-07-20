import { Injectable } from '@nestjs/common';
import { DatabaseService } from 'src/database/database.service';

@Injectable()
export class MajorsService {
  constructor(private readonly databaseService: DatabaseService) {}

  async getMajorsData(yearId: string, schoolId: string) {
    return await this.databaseService.major.findMany({
      where: {
        yearId,
        schoolId,
      },
      select: {
        id: true,
        name: true,
        logoUrl: true,
      },
    });
  }

  async getMajorData(yearId: string, schoolId: string, id: string) {
    return await this.databaseService.major.findUnique({
      where: {
        yearId_schoolId_id: {
          yearId,
          schoolId,
          id,
        },
      },
    });
  }
}
