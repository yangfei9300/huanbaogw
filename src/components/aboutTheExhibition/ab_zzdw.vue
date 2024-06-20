<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 关于展会 — 组织单位 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>组织单位</div>
		</div>

		<div  class="colonn" style="text-align: left;">
			<div       id="org-unit">
				<div       class="list-box"> 指导单位<span      >Guidance unit</span></div>
				<ul       class="list-ul">
					<li      v-for="(item,index) in zddw">{{item}}</li>
				</ul>
				<div       class="list-box"> 主办单位<span      >Organizer</span></div>
				<ul       class="list-ul">
					<li      v-for="(item,index) in zbdw">{{item}}</li>
				</ul>
				<div       class="list-box"> 承办单位<span      >Organizer</span></div>
				<ul       class="list-ul">
					<li      v-for="(item,index) in cbdw">{{item}}</li>
				</ul>
				<div       class="list-box"> 执行单位<span      >Implemented By</span></div>
				<ul       class="list-ul">
					<li      v-for="(item,index) in zxdw">{{item}}</li>
				</ul>
				<div       class="list-box"> 协办单位<span      >Co-Organizer</span></div>
				<ul       class="list-ul">
					<li      v-for="(item,index) in xbdw">{{item}}</li>
				</ul>
			</div>
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
				zddw:[
					'山东省生态环境厅'
				],
				zbdw:[
					'中国环境保护产业协会'
				],
				cbdw:['山东福瑞德国际会展集团',
					  '山东省生态环境保护促进会',
					  '山东省环境保护科学研究设计院有限公司'
				],
				zxdw:['瑞尔会展(山东) 有限公司'],
				
				xbdw:[
					'中国设备管理协会绿色安全技术服务中心',
					'山东省绿色产业与环境安全创新创业共同体',
					'山东省环境保护产业协会',
					'山东环境科学学会',
					'山东省循环经济协会',
					'山东省固废产业协会',
					'山东省水处理协会',
					'山东省建材工业协会',
					'山东省高端化工产业发展促进会',
					'青岛市环境保护产业协会'
				],
				
			}
		},
		beforeMount() {
		},
		beforeDestroy() {},
		mounted() {
		},
	
		methods: {
			topage(index) {
				this.$emit('myEvent',{index:index})
			},
			
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
	
	
	
	#org-unit           {
	    margin: 0 18.75vw;
	    margin-bottom: 2.604vw;
	    border: 1px solid #b5b2b2;
	    padding: 3.125vw 3.646vw
	}
	
	#org-unit .list-box {
	    font-size: 1.458vw;
	    border-bottom: 1px solid #b5b2b2
	}
	
	#org-unit .list-box span           {
	    font-size: 1.25vw;
	    margin-left: 1.563vw
	}
	
	#org-unit .list-ul           {
	    padding: 1.563vw 0;
	    padding-left: 1.563vw;
	    margin-bottom: .521vw
	}
	
	#org-unit .list-ul li           {
	    line-height: 1.563vw;
	    list-style: disc
	}

</style>