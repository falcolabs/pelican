import { Controller, Get, Query } from '@nestjs/common';
import { YearsService } from './years.service';

@Controller('years')
export class YearsController {
  constructor(private readonly yearsService: YearsService) {}

  @Get('/')
  async getYears(@Query('page') page: number = 1) {
    return await this.yearsService.getYears((page - 1) * 5, 5);
  }
}
