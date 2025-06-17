<script lang="ts">
    let { color, codename, displayname, slogan } = $props();
</script>

<svelte:head>
    <title>Project Pelican: Điểm đỗ và bảng điểm {displayname} CBN 2025</title>
    <meta
        name="og:title"
        content={`Project Pelican: Điểm đỗ và bảng điểm ${displayname} CBN 2025`}
    />
    <meta name="og:url" content={`https://cbn.falcolabs.org/chuyen${codename}`} />
    <meta name="og:image" content={`/banners/chuyen${codename}.png`} />
    <meta name="og:site_name" content="Project Pelican" />
    <meta
        name="og:description"
        content={`Dự án Pelican tổng hợp kết quả học sinh thi vào ${displayname} và đưa ra dự đoán điểm ${displayname} cho năm học 2025-2026.`}
    />

    <meta name="theme-color" content={color} />
    <script type="application/ld+json">
    </script>

    <meta
        name="keywords"
        content="chuyên bắc ninh, chuyên, 2025, falcolabs, dự án pelican, pelican project, CBN, điểm chuyên, điểm chuyên bắc ninh 2025, 2025"
    />
    <meta
        name="description"
        content={`Dự án Pelican tổng hợp kết quả học sinh thi vào ${displayname} và đưa ra dự đoán điểm ${displayname} cho năm học 2025-2026.`}
    />
    <meta
        name="subject"
        content={`Project Pelican: Điểm đỗ và bảng điểm ${displayname} CBN 2025`}
    />
    <meta name="copyright" content="Project Pelican - FalcoLabs Research" />
    <meta name="language" content="VI" />
    <meta name="robots" content="index,follow" />
    <meta name="revised" content="Monday, June 16th, 2025, 9:00 am" />
    <meta name="Classification" content="NNGO" />
    <meta name="author" content="name, support@falcolabs.org" />
    <meta name="copyright" content="Project Pelican - FalcoLabs Research" />
    <meta name="reply-to" content="support@falcolabs.org" />
    <meta name="owner" content="Project Pelican - FalcoLabs Research" />
    <meta name="url" content={`https://cbn.falcolabs.org/chuyen${codename}`} />
    <meta name="identifier-URL" content={`https://cbn.falcolabs.org/chuyen${codename}`} />
    <meta name="coverage" content="Worldwide" />
    <meta name="distribution" content="Global" />
</svelte:head>
