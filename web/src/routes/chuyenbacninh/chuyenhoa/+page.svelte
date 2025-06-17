<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#33B7C2";
    const CODENAME = "hoa";
    const DISPLAY_NAME = "Chuyên Hóa";
    const SLOGAN = "#hoami";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
