<script lang="ts">
    import { onMount } from "svelte";
    import Brief from "./Brief.svelte";
    import Load from "./Load.svelte";
    import Board from "./Board.svelte";
    import Seo from "./SEO.svelte";
    import Footer from "./Footer.svelte";

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
        <Brief {color} {displayname} {slogan} stats={data} />
        <h1 class="pb-1 pt-7 text-center text-2xl font-bold md:text-4xl">Bảng điểm chi tiết</h1>
        <div class="flex w-full items-center justify-center">
            <div class="flex max-w-[70vw] flex-wrap justify-center gap-1.5 pb-3">
                {#each ["json", "xlsx", "pdf", "csv", "ods"] as format}
                    <a
                        href={`/data/${codename}.${format}`}
                        role="button"
                        aria-label={`Tải xuống bảng điểm dạng ${format}`}
                        class="rounded-[9px] border border-black bg-[#F8CB47] px-6 py-3 text-[0.75rem] md:px-3 md:py-1.5"
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
        <div class="hidden w-full md:block">
            <Board {data} />
        </div>
        <div
            class="flex w-full min-w-full items-center justify-center text-center font-medium md:hidden"
        >
            <p>
                Màn hình điện thoại quá hẹp để hiển thị bảng điểm. Bạn có thể tải xuống để xem dễ
                dàng hơn.
            </p>
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
