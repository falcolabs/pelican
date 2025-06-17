<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#FE0000";
    const CODENAME = "tin";
    const DISPLAY_NAME = "Chuyên Tin";
    const SLOGAN = "#beit";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
