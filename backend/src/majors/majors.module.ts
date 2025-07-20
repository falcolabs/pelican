import { Module } from '@nestjs/common';
import { MajorsController } from './majors.controller';
import { MajorsService } from './majors.service';
import { DatabaseModule } from 'src/database/database.module';

@Module({
	imports: [DatabaseModule],
	controllers: [MajorsController],
	providers: [MajorsService],
})
export class MajorsModule {}
