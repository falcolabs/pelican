<script lang="ts">
    import { page } from "$app/state";

    import Footer from "../components/Footer.svelte";
    import NavBar from "../components/NavBar.svelte";
</script>

<svelte:head>
    <title>Ôi không, có lỗi gì đó xảy ra rồi</title>
</svelte:head>

{#if page.status === 404}
    <div class="dis flex w-full flex-col items-center justify-center gap-4 px-7 text-center">
        <h1 class="text-4xl font-bold">404 Không Tìm Thấy</h1>
        <p>
            Nội dung bạn cần tìm không có ở đây. Có thể bạn đã nhập nhầm URL hoặc bấm sai link đến
            trang.
        </p>
        <a class="text-blue-400 underline" href="mailto:support@falcolabs.org"
            >support@falcolabs.org</a
        >
        <a class="font-semibold" href="/"
            ><span class="underline">Quay về trang chủ</span>
            <i class="fa-solid fa-arrow-up-right-from-square fa-2xs"></i></a
        >
    </div>

    <style>
        .dis {
            height: calc(100vh - 7rem);
        }
    </style>
{:else}
    <h1>{page.status}</h1>
{/if}
