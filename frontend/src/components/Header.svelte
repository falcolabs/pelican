<script lang="ts">
	let hideMenu = $state(true);

	function toggleMenu() {
		hideMenu = !hideMenu;
	}

	function onScreenClick() {
		if (!hideMenu) {
			hideMenu = true;
		}
	}
</script>

<svelte:window onclickcapture={onScreenClick} />

<header
	class="fixed top-0 right-0 left-0 z-10 h-16 border-b border-b-black bg-(--accent-color) py-2 shadow-md"
>
	<div class="container mx-auto flex justify-between px-2">
		<a href="/" class="flex cursor-pointer gap-2">
			<img src="/favicon.png" alt="Pelican Logo" height="48" width="48" />
			<div class="flex flex-col justify-center leading-4 font-bold">
				<div class="m-0">PROJECT</div>
				<div class="m-0">PELICAN</div>
			</div>
		</a>

		<div class="flex items-center gap-6 max-md:hidden">
			<a href="/tou" class="hover:underline">lưu ý & điều khoản</a>
			<a href="https://github.com/falcolabs/pelican" target="_blank" class="hover:underline"
				>mã nguồn</a
			>
		</div>

		<img src="/falco-logo.svg" alt="FalcoLabs Logo" class="max-md:hidden" />

		<div class="relative md:hidden">
			<button onclick={toggleMenu} aria-label="Moblie Menu Toggle" id="mobile-menu-btn">
				<i class="fa-solid fa-bars text-5xl"></i>
			</button>

			<div
				class={`absolute right-0 flex flex-col gap-1 rounded-sm border bg-(--accent-color) px-2 py-1.5 text-nowrap ${hideMenu ? 'hidden' : ''}`}
			>
				<a href="/tou" class="underline">lưu ý & điều khoản</a>
				<a href="https://github.com/falcolabs/pelican" target="_blank" class="underline">mã nguồn</a
				>
			</div>
		</div>
	</div>
</header>
