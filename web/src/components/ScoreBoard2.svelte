<script lang="ts">
    import { onMount } from "svelte";
    import Brief2 from "./Brief2.svelte";
    import Load from "./Load.svelte";
    import Board from "./Board.svelte";
    import Seo from "./SEO.svelte";
    import Footer from "./Footer.svelte";
    import Disclaimer from "./Disclaimer.svelte";

    let { color, codename, displayname, slogan } = $props();
    let data = $state(undefined);
    onMount(() => {
        fetch(`/data/${codename}.json`).then(async (d) => {
            data = await d.json();
        });
    });
</script>

<Seo {color} {codename} {displayname} {slogan} />
<Load until={data !== undefined}>
    <div class="flex min-h-[80vh] flex-col items-center justify-start">
        <Brief2 {color} {displayname} {slogan} stats={data} />
        <h1 class="pt-7 pb-1 text-center text-2xl font-bold md:text-4xl">Bảng điểm chi tiết</h1>
        <div class="flex w-full items-center justify-center">
            <div class="flex max-w-[70vw] flex-wrap justify-center gap-1.5 pb-3">
                {#each ["json", "xlsx", "pdf", "csv", "ods"] as format}
                    <a
                        href={`/data/${codename}.${format}`}
                        role="button"
                        aria-label={`Tải xuống bảng điểm dạng ${format}`}
                        class="rounded-[9px] border border-black bg-[#F8CB47] px-3 py-1.5 text-[0.75rem]"
                        ><div
                            class="flex flex-row items-center justify-center gap-2.5 align-middle font-semibold"
                        >
                            <i class="fa-solid fa-download"></i>
                            .{format}
                        </div></a
                    >
                {/each}
            </div>
        </div>
        <Disclaimer />
        <div class="hidden w-full md:block">
            <Board {data} />
        </div>
    </div>
    <br /><br /><br />
    <div class="foot">
        <Footer />
    </div>
</Load>

<style>
    .foot {
        position: absolute;
        left: 0;
        width: 100vw;
    }
</style>
