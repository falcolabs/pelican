<script lang="ts">
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard2 from "../../components/ScoreBoard2.svelte";

    const CODENAME = "toan";
    const DISPLAY_NAME = "Chuyên Toán";
</script>

<NavBar />
<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard2 color={["#109E14", "#72001A"]} codename={CODENAME} displayname={DISPLAY_NAME} slogan={["#toantinh", "#famash"]} />
</div>
