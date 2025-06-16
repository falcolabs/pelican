<script lang="ts">
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard from "../../components/ScoreBoard.svelte";

    const COLOR = "#3F5FFF";
    const CODENAME = "ly";
    const DISPLAY_NAME = "Chuyên Lý";
    const SLOGAN = "#phily";
</script>

<NavBar />
<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
