<template>	
	<el-row>
		<el-col :offset="5" :span="12">
			<ul>
				<li 
					is="outbound-flight-summary" 
					v-for="outboundFlight in outboundFlights" 
					v-bind:outboundFlight="outboundFlight">
				</li>
			</ul>
			<el-pagination
				v-model="current"
				:page-count="totalPages"
				:page-size="perPage"
				layout="prev, pager, next"
				v-on:current-change="currentChange"
				v-bind:style="[fontStyle]"
			>
			</el-pagination>
		</el-col>
	</el-row>
</template>


<script>
export default {
	name: "outbound-flight-results",
	data: function(){
		return {
			current: parseInt(this.$route.query.page) || 1,
			perPage: 10,
			fontStyle: {
				fontSize: '16px',
				padding: '10px 75px',
				textAlign: 'center',
			}
		}
	},
	computed: {
		totalPages: function(){
			return Math.ceil(this.$store.getters.getOutboundFlights.length  / this.perPage);
		},
		outboundFlights: function(){
			var flights, chunkStart, chunkEnd;
			flights = this.$store.getters.getOutboundFlights;
			chunkStart = (this.current - 1) * this.perPage;
			chunkEnd = chunkStart + this.perPage;
			return flights.slice(chunkStart, chunkEnd);
		}
	},
	methods: {
		"currentChange": function(newPage){
			this.$set(this, "current", newPage);
		}
	},
	watch: {
		"$route": function(newRoute, oldRoute){
			this.$set(this, "current", parseInt(newRoute.query.page));
		},
		"current": function(newPage, oldPage){
			this.$router.push({"path": location.path, "query": {"page": newPage}});
		}
	}
};
</script>