<template>
    <section>
        <el-form ref="form">
            <el-col :span="9">
                <el-form-item label="资源对象">
                    <el-select v-model="form.region" placeholder="请选择资源对象">
                        <el-option label="pod" value="pod"></el-option>
                        <el-option label="node" value="node"></el-option>
						<el-option label="pv" value="pv"></el-option>
						<el-option label="npvc" value="npvc"></el-option>
						<el-option label="deployment" value="deployment"></el-option>
						<el-option label="statefulset" value="statefulset"></el-option>
						<el-option label="job" value="job"></el-option>
                    </el-select>
                </el-form-item>
            </el-col>
            <el-col :span="9">
                <el-form-item label="namespace">
                    <el-select v-model="form.region" placeholder="请选择namespace">
                        <el-option label="namespace1" value="n1"></el-option>
                        <el-option label="namespace2" value="n2"></el-option>
                    </el-select>
                </el-form-item>
            </el-col>
            <el-col :span="4">
                <el-form-item>
                    <el-button type="primary">搜索</el-button>
                    <el-button native-type="reset">重置</el-button>
                </el-form-item>
            </el-col>
        </el-form>

        <!--列表-->
		<el-table :data="users" v-loading="listLoading" highlight-current-row style="width: 100%;">
			<el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column type="index" width="60">
			</el-table-column>
			<el-table-column prop="name" label="NAME" width="120" sortable>
			</el-table-column>
			<el-table-column prop="status" label="STATUS" width="120" sortable>
			</el-table-column>
			<el-table-column prop="role" label="ROLE" width="100" sortable>
			</el-table-column>
			<el-table-column prop="age" label="AGE" width="120" sortable>
			</el-table-column>
			<el-table-column prop="version" label="VERSION" width="120" sortable>
			</el-table-column>
			<el-table-column label="操作" min-width="230">
				<template scope="scope">
					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
                    <el-button size="small" @click="handleEdit(scope.$index, scope.row)">不可调度</el-button>
				</template>
			</el-table-column>
		</el-table>
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
			</el-pagination>
		</el-col>
    </section>
</template>
<script>
    import util from '../../common/js/util'
	//import NProgress from 'nprogress'
	import { getUserListPage, removeUser, batchRemoveUser, editUser, addUser, testApi } from '../../api/api';
	export default {
		data() {
			return {
				form: {
                    region: ''
                },
                filters: {
					name: ''
				},
                users: [],
                listLoading: false,
                total: 0,
                page: 1,
			}
		},
		methods: {
			handleCurrentChange(val) {
				this.page = val;
				this.getUsers();
            },
            //获取用户列表
			getUsers() {

				let rst = testApi("123456").then(res => {
					console.log(res.data);
				});
				

				let para = {
					page: this.page,
					name: this.filters.name
				};
				this.listLoading = true;
				//NProgress.start();
				getUserListPage(para).then((res) => {
					this.total = res.data.total;
					this.users = res.data.users;
					this.listLoading = false;
					//NProgress.done();
				});
            }
        },
        mounted() {
			this.getUsers();
		}
	}

</script>