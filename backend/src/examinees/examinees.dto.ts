import { IsNotEmpty, IsNumber, IsString } from 'class-validator';

export class GetExamineesByGeneralSchoolQueries {
	@IsString()
	@IsNotEmpty()
	year: string;

	@IsString()
	@IsNotEmpty()
	school: string;

	@IsNumber()
	page: number = 1;
}

export class GetExamineesBySpecializedMajorQueries {
	@IsString()
	@IsNotEmpty()
	year: string;

	@IsString()
	@IsNotEmpty()
	school: string;

	@IsString()
	@IsNotEmpty()
	major: string;

	@IsNumber()
	page: number = 1;
}
