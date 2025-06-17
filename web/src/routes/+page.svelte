<script lang="ts">
    import HeroLinkButton from "@/components/HeroLinkButton.svelte";
    import Disclaimer from "../components/Disclaimer.svelte";
</script>

<svelte:head>
    <title>Dự án Pelican - Dự đoán & bảng điểm tuyển sinh lớp 10 tỉnh Bắc Ninh 2025</title>
</svelte:head>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <h1 class="text-center text-2xl font-bold">
        Chọn trường bạn thi để xem thông tin chi tiết và bảng điểm
    </h1>
    <Disclaimer />
    <br />
    <div class="flex flex-col flex-wrap items-center justify-center gap-4 p-8 lg:flex-row">
        <HeroLinkButton href={"/chuyenbacninh"}>
            <img src="/logos/schools/cbn_logo.jpg" alt="cbn_logo" width="64" height="64" />
            <div class="text-2xl leading-7 font-bold md:text-4xl md:leading-9">Chuyên Bắc Ninh</div>
        </HeroLinkButton>
    </div>
</div>
