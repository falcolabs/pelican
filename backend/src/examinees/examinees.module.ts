import { Module } from '@nestjs/common';
import { ExamineesService } from './examinees.service';
import { DatabaseModule } from 'src/database/database.module';
import { ExamineesController } from './examinees.controller';
import { SchoolsModule } from 'src/schools/schools.module';
import { MajorsModule } from 'src/majors/majors.module';

@Module({
	imports: [DatabaseModule],
	controllers: [ExamineesController],
	providers: [ExamineesService],
})
export class ExamineesModule {}
