<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#FE6603";
    const CODENAME = "sinh";
    const DISPLAY_NAME = "Chuyên Sinh";
    const SLOGAN = "#sinhthai";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
