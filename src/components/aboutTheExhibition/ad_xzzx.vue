<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 关于展会 — 下载中心 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>下载中心</div>
		</div>
		<div id="download-center">
			<ul id="manual">
				<li class="bj_1"
				v-for="(item,index) in files"
				>
					<div class="flex"><img
							src="data:image/png;base64,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"
							alt="" class="left-img"><span>{{item.fileName}}</span></div>
					<div class="flex"
					@click.stop="filesClick(item)"
					><span>下载</span><img
							src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAYAAAAehFoBAAAAAXNSR0IArs4c6QAABLRJREFUWEfVmderXFUUh79lx0rsXbEhdlGwKxawR0XBigXxHwnGF19FxTdfFHxQbFiiUa4tothQrFEhJiYm9pZEzZbvsk6YjGfOzJ0759y44TCXy+Hsb9ZZ67d/a00wYJVSzgAOBa4Ajga2Av4YcPuOwN/AFPAA8BYQeW2IiDJon5n+34fWrlLKBcCRwPXAicCWwJ8Dbt8hgRcBdwOvA9vk9RewNiI2zBSu7v4m4EuAY4DbEnyU/V4GFgCvAbsD+wECfw98FxHrRnlI0z1NwBcl8C35OcpeRngh8AZwEHAasBuw0jSJiC9Geci4wBdn7t6an6Ps9TxwF/Bq5v+1wOnAr8CTwKKIEH7sNSzCFpsRPnbEHZ4TOCKmSimHAXcA1wDbAi8Bjxr92UC3CazC3A7cABwIfAu8mNBLxoVuG/gm4Lqeov3atACeGTfSXQP/A6zI9HgMmHGk2wQ+PPP/RuDgvhqw8F6oIm26RMTaUeqkTWCL7ubMYfO5fwmtbhtpZXBFRPgGGlcbwAsj4pVSyv6pEPMB4d2rOu08Nb0+B1QWi/Ejj/5h0JMGtqDuTFnbCTgHODlPPPfSb7i2zktvYiG+B7wL/BgR68c9ODzpZqrD5uUCI+ympZQ9E3aXjHAFLLyGSL9h1E2PpcNgfeakI+wJp/l5qjI7pRShjOj0d+iLng7Qa11E/D4sf9sA/iSLSLf2C2ARGcFh9tIv5H3rI0JrOnBNOsJ6hmX5irWi5qPQAnvV7ef/tjfKurqI8DjvDLhprwq67p4tsiCXRcQhXQH7St14Nmt1RFiorUf455SnVXYXuZuv2tzcFdgbEGS7BhbfgBHWR7cO/BnwRLZGa3p2U87sWvTEpyT0IJhOgd8G7gUej4gfKqJSisV0Zjayl2YXMgjYlDLC/b5jk/snpRJK0T1KWkSoFNOrlGJKnAVcBVxWY4J6YToFfifbew+M5T3A9nOmg7CenBr5zSLC/ztgndZ9mcPf9ETYVt8c1rE5Nthrc4nwB8D9dsYR0QtsSgh8eQLvM1fASpDHrsepFtGUeAhYHBE2m1XRzUt7eW5aTY28Ulenx60WnQ//yWkO8GXO0hYDH/bJmjO3I9KmOu46IXV5j5pIdwL8aXYL+t+P07xsHBimtfSkc2QlrIbeaNuN9K9WgauUeB94ONucr5yj9bY4pRR1Xr+7L3B25rHQdbncKnAVnaWaddUBeDMi/jOOTeijgKtTi/3bPO40wtVmvwGmxdPAIxGhvG2ySilKmWngUOVUYOeeDmROTjrVYgnwIPAssKpKi1KKcA7GrwQcLh4wV7LWv69NpJNLHdtURKxOL6EyOFtThzXmVW9Xx91JDlcbq8fmszMzi9B5g5Lm6eYwxTmxxde0OgUWROPu5F1gB9e+/guB81IlhvBON6Gd2csKxkNETTZF7ByOz0998bA1J8B2ysIabaXLQ6OpLZqoSljVtjf+ZKB2drGWR0TdKbhx76aOY5zfOGb7pczhJpPfOKqyYIysVX5cDkGGjkPHJO6dSzjpHLiaIqyPdSit6DsU9KGj/M5WPXPYeEqo6l712bxfGRHnjwt8Ula4v4hqEUcFHifIDgwFXhMR/mo1cP0Lt6wTS83M5MwAAAAASUVORK5CYII="
							alt="" class="right-img"></div>
				</li>
				
			</ul>
		</div>
	</div>
</template>


<script>
	export default {
		name: 'Home',
		components: {
		},
		data() {
			return {
				files:[
					// {
					// 	'fileName':"邀请函.pdf",
					// 	'url':"https://shandongtibohui.zsyflive.com/profile/upload/hbgw/邀请函.pdf"
					// },
					{
						'fileName':"2023第九届绿色低碳环保产业国际博览会会刊",
						'url':"https://27476683.s21i.faiusr.com/61/ABUIABA9GAAgwPPfowYogJrc_gY.pdf"
					}
				]
			}
		},
		beforeMount() {},
		beforeDestroy() {},
		mounted() {

		},

		methods: {
			filesClick(item){
				// window.location.href=item.url;
				window.open(item.url)
			}
		}
	}
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




	#manual li {
		justify-content: space-between;
		color: #fff;
		font-size: .938vw;
		padding: .781vw 2.083vw;
		margin-bottom: 1.302vw;
		border-radius: .521vw;
		cursor: pointer
	}

	#manual li .flex,
	#manual li {
		display: flex;
		align-items: center
	}

	#manual li .left-img {
		width: 1.667vw;
		height: 1.667vw;
		margin-right: 1.042vw
	}

	#manual li .right-img {
		width: 1.25vw;
		height: 1.25vw;
		margin-left: .521vw
	}

	#manual .bj_1 {
		background: #348e42
	}

	#manual .bj_2 {
		background: #0054e0
	}

	#download-center {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 3.125vw 3.646vw
	}
</style>