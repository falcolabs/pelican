<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#000000";
    const CODENAME = "han";
    const DISPLAY_NAME = "Chuyên Hàn";
    const SLOGAN = "";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
