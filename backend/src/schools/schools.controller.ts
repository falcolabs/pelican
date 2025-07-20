import { Controller, Get, Param, NotFoundException, BadRequestException } from '@nestjs/common';
import { GetSchoolsDataParams, GetSchoolDataParams } from './schools.dto';
import { SchoolsService } from './schools.service';

@Controller('schools')
export class SchoolsController {
	constructor(private readonly schoolsService: SchoolsService) {}

	@Get('/:year')
	async getSchoolsData(@Param() params: GetSchoolsDataParams) {
		const { year } = params;

		return await this.schoolsService.getSchoolsData(year);
	}

	@Get('/:year/:id')
	async getSchoolData(@Param() params: GetSchoolDataParams) {
		const { year, id } = params;

		const schoolData = await this.schoolsService.getSchoolData(year, id);

		if (!schoolData) {
			throw new NotFoundException(`No school was found with id: ${id} in year: ${year}`);
		}

		return schoolData;
	}
}
