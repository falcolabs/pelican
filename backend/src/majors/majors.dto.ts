import { IsString, IsNotEmpty } from 'class-validator';

export class GetMajorsDataParams {
  @IsString()
  @IsNotEmpty()
  year: string;

  @IsString()
  @IsNotEmpty()
  school: string;
}
