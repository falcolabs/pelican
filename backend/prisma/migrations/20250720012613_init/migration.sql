-- CreateEnum
CREATE TYPE "Gender" AS ENUM ('MALE', 'FEMALE');

-- CreateEnum
CREATE TYPE "SchoolType" AS ENUM ('SPECIALIZED', 'GENERAL');

-- CreateEnum
CREATE TYPE "Stage" AS ENUM ('WAITING', 'GETTING', 'PROCESSING', 'READY');

-- CreateTable
CREATE TABLE "examinees" (
    "id" TEXT NOT NULL,
    "year_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "gender" "Gender" NOT NULL,
    "birth_date" TEXT NOT NULL,
    "birth_place" TEXT,
    "old_class" TEXT,
    "old_school" TEXT,
    "first_choice_school_id" TEXT,
    "priority_point" DECIMAL(4,2) NOT NULL,
    "bonus_point" DECIMAL(4,2) NOT NULL,
    "literature_point" DECIMAL(4,2) NOT NULL,
    "english_w_point" DECIMAL(4,2) NOT NULL,
    "english_mc_point" DECIMAL(4,2) NOT NULL,
    "math_w_point" DECIMAL(4,2) NOT NULL,
    "math_mc_point" DECIMAL(4,2) NOT NULL,
    "specialized_school_id" TEXT,
    "major_id" TEXT,
    "major_point" DECIMAL(4,2) NOT NULL,

    CONSTRAINT "examinees_pkey" PRIMARY KEY ("year_id","id")
);

-- CreateTable
CREATE TABLE "schools" (
    "id" TEXT NOT NULL,
    "year_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "logo_url" TEXT NOT NULL,
    "school_type" "SchoolType" NOT NULL,

    CONSTRAINT "schools_pkey" PRIMARY KEY ("year_id","id")
);

-- CreateTable
CREATE TABLE "majors" (
    "id" TEXT NOT NULL,
    "year_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "logo_url" TEXT NOT NULL,
    "school_id" TEXT NOT NULL,

    CONSTRAINT "majors_pkey" PRIMARY KEY ("year_id","school_id","id")
);

-- CreateTable
CREATE TABLE "years" (
    "id" TEXT NOT NULL,
    "stage" "Stage" NOT NULL DEFAULT 'WAITING',

    CONSTRAINT "years_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "examinees_year_id_first_choice_school_id_idx" ON "examinees"("year_id", "first_choice_school_id");

-- CreateIndex
CREATE INDEX "examinees_year_id_specialized_school_id_major_id_idx" ON "examinees"("year_id", "specialized_school_id", "major_id");

-- CreateIndex
CREATE INDEX "examinees_year_id_idx" ON "examinees"("year_id");

-- CreateIndex
CREATE INDEX "schools_year_id_idx" ON "schools"("year_id");

-- CreateIndex
CREATE INDEX "majors_year_id_school_id_idx" ON "majors"("year_id", "school_id");

-- AddForeignKey
ALTER TABLE "examinees" ADD CONSTRAINT "examinees_year_id_fkey" FOREIGN KEY ("year_id") REFERENCES "years"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "examinees" ADD CONSTRAINT "examinees_year_id_first_choice_school_id_fkey" FOREIGN KEY ("year_id", "first_choice_school_id") REFERENCES "schools"("year_id", "id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "examinees" ADD CONSTRAINT "examinees_year_id_specialized_school_id_fkey" FOREIGN KEY ("year_id", "specialized_school_id") REFERENCES "schools"("year_id", "id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "examinees" ADD CONSTRAINT "examinees_year_id_specialized_school_id_major_id_fkey" FOREIGN KEY ("year_id", "specialized_school_id", "major_id") REFERENCES "majors"("year_id", "school_id", "id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "schools" ADD CONSTRAINT "schools_year_id_fkey" FOREIGN KEY ("year_id") REFERENCES "years"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "majors" ADD CONSTRAINT "majors_year_id_fkey" FOREIGN KEY ("year_id") REFERENCES "years"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "majors" ADD CONSTRAINT "majors_year_id_school_id_fkey" FOREIGN KEY ("year_id", "school_id") REFERENCES "schools"("year_id", "id") ON DELETE RESTRICT ON UPDATE CASCADE;
