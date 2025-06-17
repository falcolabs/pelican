<script lang="ts">
    import HeroLinkButton from "@/components/HeroLinkButton.svelte";
    import Disclaimer from "../../components/Disclaimer.svelte";
    import LogoKhoiChuyen from "../../components/LogoKhoiChuyen.svelte";
</script>

<svelte:head>
    <title>Dự án Pelican - Dự đoán & bảng điểm CBN 2025</title>
</svelte:head>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <h1 class="text-center text-2xl font-bold">
        Bấm vào ô của các khối chuyên để xem thông tin chi tiết và bảng điểm
    </h1>
    <Disclaimer />
    <br />
    <div class="flex flex-col flex-wrap items-center justify-center gap-4 p-8 lg:flex-row">
        {#each [{ classes: 2, color: ["#EBEC94", "#A700FE"], displayname: "Chuyên Văn", codename: "van" }, { classes: 1, color: "#FE0000", displayname: "Chuyên Tin", codename: "tin" }, { classes: 1, color: "#3F5FFF", displayname: "Chuyên Lý", codename: "ly" }, { classes: 1, color: "#33B7C2", displayname: "Chuyên Hóa", codename: "hoa" }, { classes: 2, color: ["#109E14", "#72001A"], displayname: "Chuyên Toán", codename: "toan" }, { classes: 1, color: "#754119", displayname: "Chuyên Sử", codename: "su" }, { classes: 1, color: "#6D7075", displayname: "Chuyên Địa", codename: "dia" }, { classes: 1, color: "#FE6603", displayname: "Chuyên Sinh", codename: "sinh" }, { classes: 1, color: "#DA215B", displayname: "Chuyên Anh", codename: "anh" }, { classes: 1, color: "#010101", displayname: "Chuyên Trung", codename: "trung" }, { classes: 1, color: "#010101", displayname: "Chuyên Hàn", codename: "han" }] as { classes, color, displayname, codename }}
            {#if classes === 1}
                <HeroLinkButton href={`/chuyenbacninh/chuyen${codename}`}>
                    <LogoKhoiChuyen color={color as string} />
                    <div class="text-2xl leading-7 md:text-4xl md:leading-9">
                        Khối
                        <br />
                        <span class="font-bold" style={"color:" + color + ";"}>{displayname}</span>
                    </div>
                </HeroLinkButton>
            {:else}
                <HeroLinkButton href={`/chuyenbacninh/chuyen${codename}`}>
                    <LogoKhoiChuyen color={color[0]} />
                    <LogoKhoiChuyen color={color[1]} />
                    <div class="text-2xl leading-7 md:text-4xl md:leading-9">
                        Khối
                        <br />
                        <span class="font-bold" style={"color:" + color + ";"}>{displayname}</span>
                    </div>
                </HeroLinkButton>
            {/if}
        {/each}
    </div>
</div>
