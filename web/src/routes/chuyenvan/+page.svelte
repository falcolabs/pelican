<script lang="ts">
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard2 from "../../components/ScoreBoard2.svelte";

    const CODENAME = "van";
    const DISPLAY_NAME = "Chuyên Văn";
</script>

<NavBar />
<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard2
        color={["#DEE436", "#A700FE"]}
        codename={CODENAME}
        displayname={DISPLAY_NAME}
        slogan={["#bathoi", "#can"]}
    />
</div>
