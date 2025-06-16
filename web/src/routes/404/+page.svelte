<script lang="ts">
    import Footer from "../../components/Footer.svelte";
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard from "../../components/ScoreBoard.svelte";

    const COLOR = "#DA215B";
    const CODENAME = "anh";
    const DISPLAY_NAME = "Chuyên Anh";
    const SLOGAN = "#pinkstorm";
</script>

<svelte:head>
    <title>404 Không Tìm Thấy</title>
</svelte:head>

<NavBar />
<div class="dis flex w-full flex-col items-center justify-center px-7 text-center">
    <h1 class="text-4xl font-bold">404 Không Tìm Thấy</h1>
    <p>
        Nội dung bạn cần tìm không có ở đây. Có thể bạn đã nhập nhầm URL hoặc bấm sai link đến
        trang.
    </p>
    <a class="text-blue-400 underline" href="mailto:support@falcolabs.org">support@falcolabs.org</a>
    <a class="font-semibold" href="/"
        ><span class="underline">Quay về trang chủ</span>
        <i class="fa-solid fa-arrow-up-right-from-square fa-2xs"></i></a
    >
</div>
<Footer />

<style>
    .dis {
        height: calc(100vh - 7rem);
    }
</style>
