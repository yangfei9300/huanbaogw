<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 媒体中心 — 精彩回顾 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div> 精彩回顾</div>
		</div>


		<div id="review">
			<h2><img src="data:image/png;base64,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"
					alt=""> 展会视频 </h2>
			<div class="video-box"><video id="my-video" controls="controls" preload="auto" playsinline=""
					webkit-playsinline="" poster="/img/forum_2.167402b0.png" class="video-js">
					<source src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673512329713282.mp4#视频"
						type="video/mp4">
				</video><img src="/img/play_icon.d1ac7815.png" alt=""></div>
			<div class="line"></div>
			<h2><img src="data:image/png;base64,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"
					alt=""> 展会照片 </h2>
			<ul>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514154747640.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514154730735.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514154737871.png" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027566227.png" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027542289.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027556907.png" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027589976.png" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027562202.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/167351402757474.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027588636.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027576981.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027525848.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027531520.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027554504.jpg" alt=""></li>
				<li><img src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673514027558740.jpg" alt=""></li>
			</ul>
		</div>

	</div>
</template>

<script>
</script>

<style>
	.breadcrumb {
		height: 3.646vw;
		border-bottom: 1px solid #b5b2b2;
		font-size: .938vw;
		padding: 0 18.75vw;
		display: flex;
		align-items: center;
	}

	#overview {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;

		padding: 3.125vw 3.646vw;
		text-align: left;
	}

li{list-style-type:none;}




	#review {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 2.604vw
	}

	#review h2 {
		font-size: 1.667vw;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 1.042vw
	}

	#review h2 img {
		width: 2.5vw;
		height: 2.5vw;
		margin-right: 2.083vw
	}

	#review .video-box {
		width: 57.292vw;
		height: 32.813vw;
		position: relative;
		margin: 2.083vw auto
	}

	#review .video-box .video-js {
		width: 100%;
		height: 100%
	}

	#review .video-box .vjs-big-play-button {
		display: none
	}

	#review .video-box img {
		position: absolute;
		width: 2.552vw;
		top: calc(50% - 1.302vw);
		left: calc(50% - 1.302vw);
		pointer-events: none
	}

	#review .line {
		width: 100%;
		height: 1px;
		background: #b5b2b2;
		margin: 3.646vw 0
	}

	#review ul {
		display: flex;
		flex-wrap: wrap
	}

	#review ul li {
		display: flex;
		width: 25%;
		padding: .521vw;
		box-sizing: border-box
	}

	#review ul li img {
		width: 100%
	}

	#review ul li:nth-child(4n) {
		padding-right: 0
	}

	#review ul li:nth-child(4n+1) {
		padding-left: 0
	}
</style>