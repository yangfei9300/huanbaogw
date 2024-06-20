<template>
	<div>
		<div class="topviewbig roww">
			<img class="huiimg"
				src="https://shandongtibohui.zsyflive.com/profile/upload/hbgw/a09a6f8d37764e8076bdd5d29b255ee.png" />
			<div style="width: 1vw;"></div>
			<div style="font-size: 1.5vw;">第10届国际绿色环保产业博览会</div>
			<div class="allline"></div>
			<div class="colonn">
				<div>距离第10届国际绿色环保产业博览会开幕还有</div>
				<div style="height: 0.4vw;"></div>
				<div class="roww center_center">
					<div class="circle">{{time.days}}</div><span>天</span>
					<div class="circle">{{time.hours}}</div><span>时</span>
					<div class="circle">{{time.minutes}}</div><span>分</span>
					<div class="circle">{{time.seconds}}</div><span>秒</span>
				</div>
			</div>
		</div>


	</div>
</template>


<script>
	export default {
		name: 'Home',
		components: {},
		data() {
			return {
				banners: [
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/cf481836fc3c1cf2e8b4ef4227242d3.jpg',
				],
				time:{
					days:"",
					hours :"",
					minutes :"",
					seconds:"",
				},
				dingshiqi:null,
			}
		},
		beforeMount() {
			// 创建一个 Date 对象
			const currentDate = new Date();
			// 获取当前的年、月、日
			// const targetYear = currentDate.getFullYear(); // 获取当前年份
			// const targetMonth = currentDate.getMonth() + 1; // 获取当前月份（注意：月份是从0开始计数的，所以要加1）
			// const targetDay = currentDate.getDate(); // 获取当前是当月的第几天
			
			// const targetYear = 2024; // 获取当前年份
			// const targetMonth = 7; // 获取当前月份（注意：月份是从0开始计数的，所以要加1）
			// const targetDay = 28; // 获取当前是当月的第几天
			
			const targetYear = 2024; // 获取当前年份
			const targetMonth = 7; // 获取当前月份（注意：月份是从0开始计数的，所以要加1）
			const targetDay = 28; // 获取当前是当月的第几天
			
			
			// 创建目标日期对象
			const targetDate = new Date(targetYear, targetMonth, targetDay);
			this.dingshiqi=setInterval(res=>{
				this.calculateCountdown(targetDate);
			},1000)
			
		},
		beforeDestroy() {
			clearInterval(this.dingshiqi);
		},
		mounted() {

		},

		methods: {

			calculateCountdown(targetDate) {
				// 获取当前日期和时间
				const currentDate = new Date();
				// 计算目标日期和当前日期的时间差
				const timeDifference = targetDate - currentDate;
				// 计算剩余的天数、小时、分钟和秒数days hours minutes seconds
				const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
				const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
				const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
				const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
				console.log(",,,",days,hours,minutes,seconds);
				
				this.time.days=days;
				this.time.hours=hours;
				this.time.minutes=minutes;
				this.time.seconds=seconds;
				
			}
		}
	}
</script>

<style>
	.topviewbig {
		display: flex;
		justify-content: space-between;
		align-items: center;
		background-image: linear-gradient(90deg, #01752a, #016ac8);
		color: #fff;
		padding: 1.042vw 18.75vw;
	}

	.huiimg {
		max-height: 5.604vw;
	}

	.circle {
		font-size: 1.146vw;
		color: #0054e1;
		background: #fff;
		position: relative;
		z-index: 1;
		margin: 0 0.26vw;
		padding: 0 0.521vw;
		border-radius: 0.781vw;
		text-align: center;
	}

	span {
		margin: 0px 10px;
	}
</style>