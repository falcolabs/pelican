import { Controller, Get, Query, NotFoundException, BadRequestException } from '@nestjs/common';
import {
	GetExamineesByGeneralSchoolQueries,
	GetExamineesBySpecializedMajorQueries,
} from './examinees.dto';
import { ExamineesService } from './examinees.service';

@Controller('examinees')
export class ExamineesController {
	constructor(private readonly examineesService: ExamineesService) {}

	@Get('/general')
	async getExamineesByGeneralSchool(@Query() queries: GetExamineesByGeneralSchoolQueries) {
		const { year, school, page } = queries;

		return await this.examineesService.getExamineesByGeneralSchool(
			year,
			school.toLowerCase(),
			(page - 1) * 10,
			10,
		);
	}

	@Get('/specialized')
	async getExamineesBySpecializedMajor(@Query() queries: GetExamineesBySpecializedMajorQueries) {
		const { year, school, major, page } = queries;

		return this.examineesService.getExamineesBySpecializedMajor(
			year,
			school.toLowerCase(),
			major.toLowerCase(),
			(page - 1) * 10,
			10,
		);
	}
}
