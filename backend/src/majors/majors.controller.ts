import { Controller, Get, Param } from '@nestjs/common';
import { MajorsService } from './majors.service';
import { GetMajorsDataParams } from './majors.dto';

@Controller('majors')
export class MajorsController {
  constructor(private readonly majorsService: MajorsService) {}

  @Get('/:year/:school')
  async getMajorsData(@Param() params: GetMajorsDataParams) {
    const { year, school } = params;

    return this.majorsService.getMajorsData(year, school);
  }
}
