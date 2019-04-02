import Login from './views/Login.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import ClusterInfo from './views/info/ClusterInfo.vue'
import LogInfo from './views/log/LogInfo.vue'
import SysManage from './views/sys/SysManage.vue'
import ClusterManage from './views/manage/ClusterManage.vue'

let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    {
        path: '/',
        component: Home,
        name: '',
        iconCls: 'fa fa-tachometer',
        leaf: true,//只有一个节点
        children: [
            { path: '/clusterinfo', component: ClusterInfo, name: '查看集群信息' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: '',
        iconCls: 'fa fa-server',
        leaf: true,//只有一个节点
        children: [
            { path: '/clustermanage', component: ClusterManage, name: '集群管理' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: '',
        iconCls: 'fa fa-file-text-o',
        leaf: true,//只有一个节点
        children: [
            { path: '/loginfo', component: LogInfo, name: '日志查看' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: '',
        iconCls: 'fa fa-cog',
        leaf: true,//只有一个节点
        children: [
            { path: '/sysmanage', component: SysManage, name: '系统管理' }
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;