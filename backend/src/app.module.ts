import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { DatabaseModule } from './database/database.module';
import { SchoolsModule } from './schools/schools.module';
import { MajorsModule } from './majors/majors.module';
import { YearsModule } from './years/years.module';
import { ExamineesModule } from './examinees/examinees.module';

@Module({
	imports: [DatabaseModule, SchoolsModule, MajorsModule, YearsModule, ExamineesModule],
	controllers: [AppController],
})
export class AppModule {}
