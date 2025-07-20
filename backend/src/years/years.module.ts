import { Module } from '@nestjs/common';
import { YearsController } from './years.controller';
import { YearsService } from './years.service';
import { DatabaseModule } from 'src/database/database.module';

@Module({
  imports: [DatabaseModule],
  controllers: [YearsController],
  providers: [YearsService],
})
export class YearsModule {}
