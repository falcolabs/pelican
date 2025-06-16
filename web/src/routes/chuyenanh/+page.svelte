<script lang="ts">
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard from "../../components/ScoreBoard.svelte";

    const COLOR = "#DA215B";
    const CODENAME = "anh";
    const DISPLAY_NAME = "Chuyên Anh";
    const SLOGAN = "#pinkstorm";
</script>

<NavBar />
<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
