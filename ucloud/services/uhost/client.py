import typing


from ucloud.core.client import Client
from ucloud.services.uhost.schemas import apis


class UHostClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(UHostClient, self).__init__(config, transport, middleware, logger)

    def copy_custom_image(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CopyCustomImage - 复制自制镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SourceImageId** (str) - (Required) 源镜像Id, 参见 DescribeImage
        - **TargetProjectId** (str) - (Required) 目标项目Id, 参见 GetProjectList
        - **TargetImageDescription** (str) - 目标镜像描述
        - **TargetImageName** (str) - 目标镜像名称
        - **TargetRegion** (str) - 目标地域，不跨地域不用填
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TargetImageId** (str) - 目标镜像Id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CopyCustomImageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CopyCustomImage", d, **kwargs)
        return apis.CopyCustomImageResponseSchema().loads(resp)

    def create_custom_image(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateCustomImage - 从指定UHost实例，生成自定义镜像。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageName** (str) - (Required) 镜像名称
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **ImageDescription** (str) - 镜像描述
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **ImageId** (str) - 镜像Id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateCustomImageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCustomImage", d, **kwargs)
        return apis.CreateCustomImageResponseSchema().loads(resp)

    def create_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ CreateUHostInstance - 创建UHost实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (str) - (Required) 镜像ID。 请通过  `DescribeImage <https://docs.ucloud.cn/api/uhost-api/describe_image.html>`_ 获取
        - **LoginMode** (str) - (Required) 主机登陆模式。密码（默认选项）: Password。
        - **Password** (str) - (Required) UHost密码。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定密码。密码需使用base64进行编码，举例如下：# echo -n Password1 | base64UGFzc3dvcmQx。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **AlarmTemplateId** (int) - 告警模板id，如果传了告警模板id，且告警模板id正确，则绑定告警模板。绑定告警模板失败只会在后台有日志，不会影响创建主机流程，也不会在前端报错。
        - **BootDiskSpace** (int) - 【待废弃，不建议调用】系统盘大小。 单位：GB， 范围[20,100]， 步长：10
        - **CPU** (int) - 虚拟CPU核数。可选参数：1-64（可选范围与UHostType相关）。默认值: 4，只有Intel/Cascadelake支持CPU 64。
        - **ChargeType** (str) - 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时付费 \\ 默认为月付；\\ >Postpay ，后付费。
        - **CouponId** (str) - 主机代金券ID。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **DiskPassword** (str) - 【待废弃，不建议调用】加密盘的密码。若输入此字段，自动选择加密盘。加密盘需要权限位。
        - **DiskSpace** (int) - 【待废弃，不建议调用】数据盘大小。 单位：GB， 范围[0,8000]， 步长：10， 默认值：20，云盘支持0-8000；本地普通盘支持0-2000；本地SSD盘（包括所有GPU机型）支持100-1000
        - **Disks** (list) - 见 **CreateUHostInstanceParamDisks** 模型定义
        - **GPU** (int) - GPU卡核心数。仅GPU机型支持此字段（可选范围与UHostType相关）
        - **GpuType** (str) - GPU类型，枚举值["K80", "P40", "V100"]
        - **HostType** (str) - 【已废弃】宿主机类型，N2，N1
        - **HotplugFeature** (bool) - 【待废弃，不建议调用】是否开启热升级特性。True为开启，False为未开启，默认False。仅系列1云主机需要使用此字段，系列2云主机根据镜像是否支持云主机。
        - **InstallAgent** (str) - 【暂不支持】是否安装UGA。'yes': 安装；其他或者不填：不安装。
        - **IsolationGroup** (str) - 硬件隔离组id。可通过DescribeIsolationGroup获取。
        - **KeyPair** (str) - 【暂不支持】Keypair公钥，LoginMode为KeyPair时此项必须
        - **MachineType** (str) - 云主机类型，枚举值["N", "C", "G", "O"]
        - **MaxCount** (int) - 【批量创建主机时必填】最大创建主机数量，取值范围是[1,100];
        - **Memory** (int) - 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值：8192
        - **MinimalCpuPlatform** (str) - 最低cpu平台，枚举值["Intel/Auto", "Intel/IvyBridge", "Intel/Haswell", "Intel/Broadwell", "Intel/Skylake", "Intel/Cascadelake"(只有O型云主机可选)]
        - **Name** (str) - UHost实例名称。默认：UHost。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定实例名称。
        - **NetCapability** (str) - 网络增强。枚举值：Normal（默认），不开启;  Super，开启网络增强1.0； Ultra，开启网络增强2.0（仅支持部分可用区，请参考控制台）
        - **NetworkId** (str) - 【已废弃】网络ID（VPC2.0情况下无需填写）。VPC1.0情况下，若不填写，代表优先选择基础网络； 若填写，代表选择子网。参见DescribeSubnet。
        - **NetworkInterface** (list) - 见 **CreateUHostInstanceParamNetworkInterface** 模型定义
        - **PrivateIp** (list) - 【数组】创建云主机时指定内网IP。若不传值，则随机分配当前子网下的IP。调用方式举例：PrivateIp.0=x.x.x.x。当前只支持一个内网IP。
        - **PrivateMac** (str) - 【批量创建该参数无效】【内部字段】创建云主机时指定Mac。调用方式举例：PrivateMac="xx:xx:xx:xx:xx:xx"。
        - **Quantity** (int) - 购买时长。默认:值 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表购买至月末。
        - **ResourceType** (int) - 【内部参数】资源类型
        - **SecurityGroupId** (str) - 防火墙Id，默认：Web推荐防火墙。如何查询SecurityGroupId请参见  `DescribeSecurityGroup <https://docs.ucloud.cn/api/unet-api/describe_security_group.html>`_ 。
        - **SetId** (int) - 
        - **StorageType** (str) - 【待废弃，不建议调用】磁盘类型，同时设定系统盘和数据盘的磁盘类型。枚举值为：LocalDisk，本地磁盘; UDisk，云硬盘；默认为LocalDisk。仅部分可用区支持云硬盘方式的主机存储方式，具体请查询控制台。
        - **SubnetId** (str) - 子网 ID。默认为当前地域的默认子网。
        - **Tag** (str) - 业务组。默认：Default（Default即为未分组）。请遵照 `字段规范 <https://docs.ucloud.cn/api/uhost-api/specification>`_ 设定业务组。
        - **TimemachineFeature** (str) - 【待废弃，不建议调用】是否开启方舟特性。Yes为开启方舟，No为关闭方舟。目前仅选择普通本地盘+普通本地盘 或 SSD云盘+普通云盘的组合支持开启方舟。
        - **UHostType** (str) - 云主机机型。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。【待废弃，不建议调用】
        - **UserDataScript** (str) - 【暂不支持】cloudinit方式下，用户初始化脚本
        - **VPCId** (str) - VPC ID。默认为当前地域的默认VPC。
        
        **Response**

        - **UHostIds** (list) - UHost实例Id集合
        - **IPs** (list) - 【批量创建不会返回】IP信息
        
        **Request Model**
        
        **CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSH** 
        
        - **AreaCode** (str) - AreaCode, 区域航空港国际通用代码。Area和AreaCode两者必填一个
        - **Port** (int) - SSH端口，1-65535且不能使用80，443端口
        - **Area** (str) - 填写支持SSH访问IP的地区名称，如“洛杉矶”，“新加坡”，“香港”，“东京”，“华盛顿”，“法兰克福”。Area和AreaCode两者必填一个

        **CreateUHostInstanceParamNetworkInterfaceEIP** 
        
        - **OperatorName** (str) - 【如果绑定EIP这个参数必填】弹性IP的线路如下: 国际: International BGP: Bgp 各地域允许的线路参数如下: cn-sh1: Bgp cn-sh2: Bgp cn-gd: Bgp cn-bj1: Bgp cn-bj2: Bgp hk: International us-ca: International th-bkk: International kr-seoul:International us-ws:International ge-fra:International sg:International tw-kh:International.其他海外线路均为 International
        - **PayMode** (str) - 弹性IP的计费模式. 枚举值: "Traffic", 流量计费; "Bandwidth", 带宽计费; "ShareBandwidth",共享带宽模式. "Free":免费带宽模式.默认为 "Bandwidth".
        - **ShareBandwidthId** (str) - 绑定的共享带宽Id，仅当PayMode为ShareBandwidth时有效
        - **CouponId** (str) - 当前EIP代金券id。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **Bandwidth** (int) - 【如果绑定EIP这个参数必填】弹性IP的外网带宽, 单位为Mbps. 共享带宽模式必须指定0M带宽, 非共享带宽模式必须指定非0Mbps带宽. 各地域非共享带宽的带宽范围如下： 流量计费[1-300]，带宽计费[1-800]
        - **GlobalSSH** (dict) - 见 **CreateUHostInstanceParamNetworkInterfaceEIPGlobalSSH** 模型定义

        **CreateUHostInstanceParamNetworkInterface** 
        
        - **EIP** (dict) - 见 **CreateUHostInstanceParamNetworkInterfaceEIP** 模型定义

        **CreateUHostInstanceParamDisks** 
        
        - **Type** (str) - 磁盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **Encrypted** (bool) - 加密：true, 不加密: false加密必须传入对应的的KmsKeyId
        - **Size** (int) - 磁盘大小，单位GB。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **KmsKeyId** (str) - kms的id
        - **CouponId** (str) - 云盘代金券id。不适用于系统盘/本地盘。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **BackupType** (str) - 磁盘备份方案。枚举值：\\ > NONE，无备份 \\ > DATAARK，数据方舟 \\ 当前磁盘支持的备份模式参考  `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 
        - **IsBoot** (str) - 是否是系统盘。枚举值：\\ > True，是系统盘 \\ > False，是数据盘（默认）。Disks数组中有且只能有一块盘是系统盘。

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUHostInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUHostInstance", d, **kwargs)
        return apis.CreateUHostInstanceResponseSchema().loads(resp)

    def describe_image(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeImage - 获取指定数据中心镜像列表，用户可通过指定操作系统类型，镜像Id进行过滤。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (str) - 镜像Id
        - **ImageType** (str) - 镜像类型。标准镜像：Base，镜像市场：Business， 自定义镜像：Custom，默认返回所有类型
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        - **OsType** (str) - 操作系统类型：Linux， Windows 默认返回所有类型
        - **PriceSet** (int) - 是否返回价格：1返回，0不返回；默认不返回
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - 满足条件的镜像总数
        - **ImageSet** (list) - 见 **UHostImageSet** 模型定义
        
        **Response Model**
        
        **UHostImageSet** 
        
        - **Vendor** (str) - 供应商（仅行业镜像将返回这个值）
        - **State** (str) - 镜像状态， 可用：Available，制作中：Making， 不可用：Unavailable
        - **OsName** (str) - 操作系统名称
        - **FuncType** (str) - 行业镜像类型（仅行业镜像将返回这个值）
        - **ImageDescription** (str) - 镜像描述
        - **Zone** (str) - 可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_  |
        - **ImageId** (str) - 镜像ID
        - **ImageName** (str) - 镜像名称
        - **OsType** (str) - 操作系统类型：Liunx，Windows
        - **Features** (list) - 特殊状态标识， 目前包含NetEnhnced（网络增强1.0）, NetEnhanced_Ultra]（网络增强2.0）
        - **CreateTime** (int) - 创建时间，格式为Unix时间戳
        - **ImageSize** (int) - 镜像大小
        - **MinimalCPU** (str) - 默认值为空'''。当CentOS 7.3/7.4/7.5等镜像会标记为“Broadwell”
        - **ImageType** (str) - 镜像类型 标准镜像：Base， 行业镜像：Business，自定义镜像：Custom
        - **IntegratedSoftware** (str) - 集成软件名称（仅行业镜像将返回这个值）
        - **Links** (str) - 介绍链接（仅行业镜像将返回这个值）

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeImageRequestSchema().dumps(d)

        resp = self.invoke("DescribeImage", d, **kwargs)
        return apis.DescribeImageResponseSchema().loads(resp)

    def describe_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeUHostInstance - 获取主机或主机列表信息，并可根据数据中心，主机ID等参数进行过滤。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **IsolationGroup** (str) - 硬件隔离组id。通过硬件隔离组筛选主机。
        - **LifeCycle** (int) - 1：普通云主机；2：抢占型云主机；如不传此参数，默认全部获取
        - **Limit** (int) - 返回数据长度，默认为20，最大100
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        - **SubnetId** (str) - 子网id。通过子网筛选主机。北京一地域无效。
        - **Tag** (str) - 要查询的业务组名称
        - **UHostIds** (list) - 【数组】UHost主机的资源ID，例如UHostIds.0代表希望获取信息 的主机1，UHostIds.1代表主机2。 如果不传入，则返回当前Region 所有符合条件的UHost实例。
        - **VPCId** (str) - vpc id。通过VPC筛选主机。北京一地域无效。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - UHostInstance总数
        - **UHostSet** (list) - 见 **UHostInstanceSet** 模型定义
        
        **Response Model**
        
        **UHostDiskSet** 
        
        - **BackupType** (str) - 备份方案。若开通了数据方舟，则为DataArk
        - **IsBoot** (str) - 是否是系统盘。枚举值：\\ > True，是系统盘 \\ > False，是数据盘（默认）。Disks数组中有且只能有一块盘是系统盘。
        - **Encrypted** (bool) - true: 加密盘 false：非加密盘
        - **Type** (str) - 【建议不再使用】磁盘类型。系统盘: Boot，数据盘: Data,网络盘：Udisk
        - **Name** (str) - UDisk名字（仅当磁盘是UDisk时返回）
        - **Drive** (str) - 磁盘盘符
        - **DiskType** (str) - 磁盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **DiskId** (str) - 磁盘ID
        - **Size** (int) - 磁盘大小，单位: GB

        **UHostIPSet** 
        
        - **IPId** (str) - IP资源ID (内网IP无对应的资源ID)
        - **IP** (str) - IP地址
        - **Bandwidth** (int) - IP对应的带宽, 单位: Mb (内网IP不显示带宽信息)
        - **Default** (str) - 是否默认的弹性网卡的信息。true: 是默认弹性网卡；其他值：不是。
        - **VPCId** (str) - IP地址对应的VPC ID（北京一当前字段为空）
        - **SubnetId** (str) - IP地址对应的子网 ID（北京一当前字段为空）
        - **Type** (str) - 国际: Internation，BGP: Bgp，内网: Private

        **UHostInstanceSet** 
        
        - **UHostType** (str) - 【建议不再使用】云主机机型（旧）。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。
        - **BasicImageName** (str) - 基础镜像名称（指当前自定义镜像的来源镜像）
        - **OsName** (str) - 创建主机的最初来源镜像的操作系统名称（若直接通过基础镜像创建，此处返回和BasicImageName一致）
        - **ImageId** (str) - 【建议不再使用】主机的系统盘ID。
        - **GPU** (int) - GPU个数
        - **CPU** (int) - 虚拟CPU核数，单位: 个
        - **Memory** (int) - 内存大小，单位: MB
        - **TotalDiskSpace** (int) - 总的数据盘存储空间。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Remark** (str) - 备注
        - **ExpireTime** (int) - 到期时间，格式为Unix时间戳
        - **CreateTime** (int) - 创建时间，格式为Unix时间戳
        - **LifeCycle** (str) - 主机的生命周期类型。目前仅支持Normal：普通；
        - **ChargeType** (str) - 计费模式，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费（需开启权限）；
        - **NetCapability** (str) - 网络增强。Normal: 无；Super： 网络增强1.0； Ultra: 网络增强2.0
        - **BootDiskState** (str) - 系统盘状态 Normal表示初始化完成；Initializing表示在初始化。仍在初始化的系统盘无法制作镜像。
        - **IPSet** (list) - 见 **UHostIPSet** 模型定义
        - **SubnetType** (str) - 【建议不再使用】仅北京A的云主机会返回此字段。基础网络模式：Default；子网模式：Private
        - **HostType** (str) - 【建议不再使用】主机系列：N2，表示系列2；N1，表示系列1
        - **IsolationGroup** (str) - 隔离组id，不在隔离组则返回""
        - **BasicImageId** (str) - 基础镜像ID（指当前自定义镜像的来源镜像）
        - **Tag** (str) - 业务组名称
        - **Name** (str) - UHost实例名称
        - **TimemachineFeature** (str) - 【建议不再使用】数据方舟模式。枚举值：\\ > Yes: 开启方舟； \\ > no，未开启方舟
        - **OsType** (str) - 操作系统类别。返回"Linux"或者"Windows"
        - **MachineType** (str) - 云主机机型（新）。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type#主机概念20版本>`_ 。
        - **StorageType** (str) - 【建议不再使用】主机磁盘类型。 枚举值为：\\ > LocalDisk，本地磁盘; \\ > UDisk 云盘。\\只要有一块磁盘为本地盘，即返回LocalDisk。
        - **AutoRenew** (str) - 是否自动续费，自动续费：“Yes”，不自动续费：“No”
        - **NetworkState** (str) - 【建议不再使用】网络状态。 连接：Connected， 断开：NotConnected
        - **HotplugFeature** (bool) - true: 开启热升级； false，未开启热升级
        - **UHostId** (str) - UHost实例ID
        - **State** (str) - 实例状态，枚举值：\\ >初始化: Initializing; \\ >启动中: Starting; \\> 运行中: Running; \\> 关机中: Stopping; \\ >关机: Stopped \\ >安装失败: Install Fail; \\ >重启中: Rebooting
        - **DiskSet** (list) - 见 **UHostDiskSet** 模型定义

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUHostInstance", d, **kwargs)
        return apis.DescribeUHostInstanceResponseSchema().loads(resp)

    def describe_uhost_tags(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUHostTags - 获取指定数据中心的业务组列表。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - 已有主机的业务组总个数
        - **TagSet** (list) - 见 **UHostTagSet** 模型定义
        
        **Response Model**
        
        **UHostTagSet** 
        
        - **Zone** (str) - 可用区
        - **Tag** (str) - 业务组名称
        - **TotalCount** (int) - 该业务组中包含的主机个数

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUHostTagsRequestSchema().dumps(d)

        resp = self.invoke("DescribeUHostTags", d, **kwargs)
        return apis.DescribeUHostTagsResponseSchema().loads(resp)

    def get_uhost_instance_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUHostInstancePrice - 根据UHost实例配置，获取UHost实例的价格。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **CPU** (int) - (Required) 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值: 4
        - **Count** (int) - (Required) 【未启用】购买台数，范围[1,5]
        - **ImageId** (str) - (Required) 镜像Id，可通过  `DescribeImage <https://docs.ucloud.cn/api/uhost-api/describe_image.html>`_  获取镜像ID
        - **Memory** (int) - (Required) 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值：8192
        - **ChargeType** (str) - 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时付费 \\ 默认为月付。
        - **DiskSpace** (int) - 【待废弃】数据盘大小，单位: GB，范围[0,1000]，步长: 10，默认值: 0
        - **Disks** (list) - 见 **GetUHostInstancePriceParamDisks** 模型定义
        - **GPU** (int) - GPU卡核心数。仅GPU机型支持此字段（可选范围与UHostType相关）。
        - **GpuType** (str) - GPU类型，枚举值["K80", "P40", "V100"]
        - **LifeCycle** (int) - 【未支持】1：普通云主机；2：抢占性云主机；默认普通
        - **MachineType** (str) - 云主机类型，枚举值["N", "C", "G", "O"]
        - **NetCapability** (str) - 网络增强。枚举值：Normal，不开启; Super，开启网络增强1.0; Ultra，开启网络增强2.0； 默认值为Normal。Normal和Ultra不计费。
        - **Quantity** (int) - 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末。
        - **StorageType** (str) - 【待废弃】磁盘类型，同时设定系统盘和数据盘， 枚举值为：LocalDisk，本地磁盘; UDisk，云硬盘; 默认为LocalDisk 仅部分可用区支持云硬盘方式的主机存储方式，具体请查询控制台。
        - **TimemachineFeature** (str) - 【待废弃】方舟机型。No，Yes。默认是No。
        - **UHostType** (str) - 云主机机型。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PriceSet** (list) - 见 **UHostPriceSet** 模型定义
        
        **Request Model**
        
        **GetUHostInstancePriceParamDisks** 
        
        - **Size** (int) - 磁盘大小，单位GB。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **Type** (str) - 磁盘类型。请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **IsBoot** (str) - 是否是系统盘。枚举值：\\ > True，是系统盘 \\ > False，是数据盘（默认）。Disks数组中有且只能有一块盘是系统盘。
        - **BackupType** (str) - 磁盘备份方案。枚举值：\\ > NONE，无备份 \\ > DATAARK，数据方舟 \\ 当前磁盘支持的备份模式参考  `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 

        **Response Model**
        
        **UHostPriceSet** 
        
        - **ChargeType** (str) - 计费类型。Year，Month，Dynamic
        - **Price** (float) - 价格，单位: 元，保留小数点后两位有效数字

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostInstancePriceRequestSchema().dumps(d)

        resp = self.invoke("GetUHostInstancePrice", d, **kwargs)
        return apis.GetUHostInstancePriceResponseSchema().loads(resp)

    def get_uhost_instance_vnc_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUHostInstanceVncInfo - 获取指定UHost实例的管理VNC配置详细信息。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **VncIP** (str) - Vnc登录IP
        - **VncPort** (int) - Vnc登录端口
        - **VncPassword** (str) - Vnc 登录密码
        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostInstanceVncInfoRequestSchema().dumps(d)

        resp = self.invoke("GetUHostInstanceVncInfo", d, **kwargs)
        return apis.GetUHostInstanceVncInfoResponseSchema().loads(resp)

    def get_uhost_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUHostUpgradePrice - 获取UHost实例升级配置的价格。可选配置范围请参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID。 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 。
        - **BootDiskSpace** (int) - 【待废弃】系统大小，单位: GB，范围[20,100]，步长: 10。
        - **CPU** (int) - 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值为当前实例的CPU核数。
        - **DiskSpace** (int) - 【待废弃】数据盘大小，单位: GB，范围[0,1000]，步长: 10， 默认值是该主机当前数据盘大小。
        - **HostType** (str) - 【待废弃】主机系列，目前支持N1,N2
        - **Memory** (int) - 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值为当前实例的内存大小。
        - **NetCapValue** (int) - 网卡升降级（1，表示升级，2表示降级，0表示不变）
        - **TimemachineFeature** (str) - 方舟机型。No，Yes。默认是No。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **Price** (float) - 规格调整差价。精确到小数点后2位。
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUHostUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetUHostUpgradePrice", d, **kwargs)
        return apis.GetUHostUpgradePriceResponseSchema().loads(resp)

    def import_custom_image(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ImportCustomImage - 把UFile的镜像文件导入到UHost，生成自定义镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Auth** (bool) - (Required) 是否授权。必须填true
        - **Format** (str) - (Required) 镜像格式，可选RAW、VHD、VMDK、qcow2
        - **ImageName** (str) - (Required) 镜像名称
        - **OsName** (str) - (Required) 操作系统详细版本，请参考控制台的镜像版本；OsType为Other时，输入参数为Other
        - **OsType** (str) - (Required) 操作系统平台，比如CentOS、Ubuntu、Windows、RedHat等，请参考控制台的镜像版本；若导入控制台上没有的操作系统，参数为Other
        - **UFileUrl** (str) - (Required) UFile私有空间地址
        - **ImageDescription** (str) - 镜像描述
        
        **Response**

        - **ImageId** (str) - 镜像Id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ImportCustomImageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ImportCustomImage", d, **kwargs)
        return apis.ImportCustomImageResponseSchema().loads(resp)

    def modify_uhost_instance_name(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUHostInstanceName - 修改指定UHost实例名称，需要给出数据中心，UHostId，及新的实例名称。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Name** (str) - UHost实例名称
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceNameRequestSchema().dumps(d)

        resp = self.invoke("ModifyUHostInstanceName", d, **kwargs)
        return apis.ModifyUHostInstanceNameResponseSchema().loads(resp)

    def modify_uhost_instance_remark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUHostInstanceRemark - 修改指定UHost实例备注信息。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Remark** (str) - 备注
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceRemarkRequestSchema().dumps(d)

        resp = self.invoke("ModifyUHostInstanceRemark", d, **kwargs)
        return apis.ModifyUHostInstanceRemarkResponseSchema().loads(resp)

    def modify_uhost_instance_tag(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUHostInstanceTag - 修改指定UHost实例业务组标识。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Tag** (str) - 业务组名称
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUHostInstanceTagRequestSchema().dumps(d)

        resp = self.invoke("ModifyUHostInstanceTag", d, **kwargs)
        return apis.ModifyUHostInstanceTagResponseSchema().loads(resp)

    def poweroff_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ PoweroffUHostInstance - 直接关闭UHost实例电源，无需等待实例正常关闭。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PoweroffUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("PoweroffUHostInstance", d, **kwargs)
        return apis.PoweroffUHostInstanceResponseSchema().loads(resp)

    def reboot_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ RebootUHostInstance - 重新启动UHost实例，需要指定数据中心及UHostID两个参数的值。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **DiskPassword** (str) - 加密盘密码
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RebootUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("RebootUHostInstance", d, **kwargs)
        return apis.RebootUHostInstanceResponseSchema().loads(resp)

    def reinstall_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ReinstallUHostInstance - 重新安装指定UHost实例的操作系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例资源ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **BootDiskSpace** (int) - 系统盘大小。 单位：GB， 范围[20,100]， 步长：10
        - **DNSServers** (list) - 针对非私有子网主机，可自定义DNS。n可为0-2
        - **ImageId** (str) - 镜像Id，默认使用原镜像 参见  `DescribeImage <https://docs.ucloud.cn/api/uhost-api/describe_image.html>`_ 
        - **Password** (str) - 如果创建UHost实例时LoginMode为Password，则必须填写，如果LoginMode为KeyPair，不需要填写 （密码格式使用BASE64编码；LoginMode不可变更）
        - **ReserveDisk** (str) - 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes；如果是从Windows重装为Linux或反之，则无法保留数据盘
        - **ResourceType** (int) - 云灾备指明191
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例资源ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReinstallUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("ReinstallUHostInstance", d, **kwargs)
        return apis.ReinstallUHostInstanceResponseSchema().loads(resp)

    def reset_uhost_instance_password(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ResetUHostInstancePassword - 重置UHost实例的管理员密码。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Password** (str) - (Required) UHost新密码（密码格式使用BASE64编码）
        - **UHostId** (str) - (Required) UHost实例ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResetUHostInstancePasswordRequestSchema().dumps(d)

        resp = self.invoke("ResetUHostInstancePassword", d, **kwargs)
        return apis.ResetUHostInstancePasswordResponseSchema().loads(resp)

    def resize_attached_disk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ResizeAttachedDisk - 修改挂载的磁盘大小，包含系统盘和数据盘

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DiskId** (str) - (Required) 磁盘ID。参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 返回值中的DiskSet。
        - **DiskSpace** (int) - (Required) 磁盘大小，单位GB，步长为10。取值范围需大于当前磁盘大小，最大值请参考 `磁盘类型 <https://docs.ucloud.cn/api/uhost-api/disk_type>`_ 。
        - **UHostId** (str) - (Required) UHost实例ID。 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DiskId** (str) - 改配成功的磁盘id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeAttachedDiskRequestSchema().dumps(d)

        resp = self.invoke("ResizeAttachedDisk", d, **kwargs)
        return apis.ResizeAttachedDiskResponseSchema().loads(resp)

    def resize_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ResizeUHostInstance - 修改指定UHost实例的资源配置，如CPU核心数，内存容量大小，网络增强等。可选配置范围请参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **BootDiskSpace** (int) - 【待废弃】系统盘大小，单位：GB，范围[20,100]，步长：10，系统盘不支持缩容，因此不允许输入比当前实例系统盘小的值
        - **CPU** (int) - 虚拟CPU核数。可选参数：1-32（可选范围与UHostType相关）。默认值为当前实例的CPU核数
        - **DiskSpace** (int) - 【待废弃】数据盘大小，单位：GB，范围[10,1000]； SSD机型，单位：GB，范围[100,500]；步长：10，默认值为当前实例的数据盘大小，数据盘不支持缩容，因此不允许输入比当前实例数据盘大小的值
        - **Memory** (int) - 内存大小。单位：MB。范围 ：[1024, 262144]，取值为1024的倍数（可选范围与UHostType相关）。默认值为当前实例的内存大小。
        - **NetCapValue** (int) - 网卡升降级（1，表示升级，2表示降级，0表示不变）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("ResizeUHostInstance", d, **kwargs)
        return apis.ResizeUHostInstanceResponseSchema().loads(resp)

    def start_uhost_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ StartUHostInstance - 启动处于关闭状态的UHost实例，需要指定数据中心及UHostID两个参数的值。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **DiskPassword** (str) - 加密盘密码
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("StartUHostInstance", d, **kwargs)
        return apis.StartUHostInstanceResponseSchema().loads(resp)

    def stop_uhost_instance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ StopUHostInstance - 指停止处于运行状态的UHost实例，需指定数据中心及UhostID。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost实例ID 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UhostId** (str) - UHost实例ID
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StopUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("StopUHostInstance", d, **kwargs)
        return apis.StopUHostInstanceResponseSchema().loads(resp)

    def terminate_custom_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ TerminateCustomImage - 删除用户自定义镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (str) - (Required) 自制镜像ID 参见  `DescribeImage <https://docs.ucloud.cn/api/uhost-api/describe_image.html>`_ 
        
        **Response**

        - **ImageId** (str) - 自制镜像Id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminateCustomImageRequestSchema().dumps(d)

        resp = self.invoke("TerminateCustomImage", d, **kwargs)
        return apis.TerminateCustomImageResponseSchema().loads(resp)

    def terminate_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ TerminateUHostInstance - 删除指定数据中心的UHost实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostId** (str) - (Required) UHost资源Id 参见  `DescribeUHostInstance <https://docs.ucloud.cn/api/uhost-api/describe_uhost_instance.html>`_ 
        - **Destroy** (int) - 是否直接删除，0表示按照原来的逻辑（有回收站权限，则进入回收站），1表示直接删除
        - **ReleaseEIP** (bool) - 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        - **ReleaseUDisk** (bool) - 是否删除挂载的数据盘。true删除，其他不删除。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **InRecycle** (str) - 放入回收站:"Yes", 彻底删除：“No”
        - **UHostId** (str) - UHost 实例 Id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminateUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("TerminateUHostInstance", d, **kwargs)
        return apis.TerminateUHostInstanceResponseSchema().loads(resp)

    def upgrade_to_ark_uhost_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ UpgradeToArkUHostInstance - 普通升级为方舟机型

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UHostIds** (list) - (Required) UHost主机的资源ID，例如UHostIds.0代表希望升级的主机1，UHostIds.1代表主机2。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **CouponId** (str) - 代金券ID 请参考DescribeCoupon接口
        
        **Response**

        - **UHostSet** (list) - UHost主机的资源ID数组
        
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.UpgradeToArkUHostInstanceRequestSchema().dumps(d)

        resp = self.invoke("UpgradeToArkUHostInstance", d, **kwargs)
        return apis.UpgradeToArkUHostInstanceResponseSchema().loads(resp)
