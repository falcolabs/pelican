import { IsNotEmpty, IsString } from 'class-validator';

export class GetSchoolsDataParams {
  @IsString()
  @IsNotEmpty()
  year: string;
}

export class GetSchoolDataParams extends GetSchoolsDataParams {
  @IsString()
  @IsNotEmpty()
  id: string;
}
