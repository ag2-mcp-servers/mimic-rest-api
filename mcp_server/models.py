# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T19:25:26+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel


class AccessEntry(BaseModel):
    access_mask: Optional[str] = None
    agent_range: Optional[str] = None
    user: Optional[str] = None


class AgentState(BaseModel):
    agentNum: Optional[int] = None
    state: Optional[int] = None


class ConfigCOAP(BaseModel):
    keystore: Optional[str] = None
    primary_port: Optional[int] = None
    rule: Optional[str] = None
    secure_port: Optional[int] = None


class ConfigDHCP(BaseModel):
    add_options: Optional[str] = None
    classid: Optional[str] = None
    hwaddr: Optional[str] = None
    script: Optional[str] = None


class ConfigIPMI(BaseModel):
    primary_port: Optional[int] = None
    secure_port: Optional[int] = None
    version: Optional[str] = None


class ConfigMQTT(BaseModel):
    broker: Optional[str] = None
    clientid: Optional[str] = None
    filename: Optional[str] = None
    is_tls: Optional[str] = None
    password: Optional[str] = None
    port: Optional[int] = None
    tls_conf_filename: Optional[str] = None
    username: Optional[str] = None
    version: Optional[str] = None


class ConfigNETFLOW(BaseModel):
    bundleflowsets: Optional[int] = None
    collector: Optional[str] = None
    collectorport: Optional[int] = None
    filename: Optional[str] = None


class ConfigPROXY(BaseModel):
    TCP_NODELAY: Optional[int] = None
    client_to_server: Optional[str] = None
    disconnect_delay: Optional[int] = None
    max_connects: Optional[int] = None
    portno: Optional[int] = None
    pre_connect: Optional[str] = None
    server_to_client: Optional[str] = None
    target: Optional[str] = None
    transport: Optional[str] = None


class ConfigSFLOW(BaseModel):
    collector: Optional[str] = None
    collectorport: Optional[int] = None
    encoding_type: Optional[str] = None
    filename: Optional[str] = None
    flows_per_min: Optional[int] = None
    include_samples: Optional[str] = None
    records_per_sample: Optional[str] = None
    samples_per_datagram: Optional[str] = None


class ConfigSNMPTCP(BaseModel):
    connections: Optional[int] = None


class ConfigSNMPv3(BaseModel):
    context_engine_id: Optional[str] = None
    engine_id: Optional[str] = None
    usm_db: Optional[str] = None
    vacm_db: Optional[str] = None


class ConfigSSH(BaseModel):
    port: Optional[int] = None
    version: Optional[str] = None


class ConfigSYSLOG(BaseModel):
    client: Optional[str] = None
    hostname: Optional[str] = None
    localport: Optional[int] = None
    separator: Optional[str] = None
    sequence: Optional[int] = None
    server: Optional[str] = None
    serverport: Optional[int] = None
    timestamp: Optional[str] = None


class ConfigTELNET(BaseModel):
    keymap: Optional[str] = None
    paging_prompt: Optional[str] = None
    port: Optional[int] = None
    prompt: Optional[str] = None
    rule: Optional[str] = None
    userdb: Optional[str] = None


class ConfigTFTP(BaseModel):
    cache: Optional[int] = None
    client: Optional[str] = None
    dstfile: Optional[str] = None
    mode: Optional[str] = None
    port: Optional[int] = None
    retries: Optional[int] = None
    script: Optional[str] = None
    server: Optional[str] = None
    srcfile: Optional[str] = None
    timeout: Optional[int] = None
    trace: Optional[str] = None


class ConfigTOD(BaseModel):
    port: Optional[int] = None
    retries: Optional[int] = None
    script: Optional[str] = None
    server: Optional[str] = None
    timeout: Optional[int] = None


class ConfigWEB(BaseModel):
    is_persistent_connections: Optional[int] = None
    password: Optional[str] = None
    port: Optional[int] = None
    rule: Optional[str] = None
    username: Optional[str] = None
    wsdl: Optional[str] = None


class IPAlias(BaseModel):
    IP: Optional[str] = None
    interface: Optional[str] = None
    mask: Optional[str] = None
    port: Optional[int] = None


class IPSource(BaseModel):
    IP: Optional[str] = None
    port: Optional[int] = None


class SyslogMsg(BaseModel):
    hostname: Optional[str] = None
    message: Optional[str] = None
    separator: Optional[str] = None
    sequence: Optional[str] = None
    timestamp: Optional[str] = None


class TelnetUser(BaseModel):
    groups: Optional[List[str]] = None
    hasPassword: Optional[int] = None
    password: Optional[str] = None
    username: Optional[str] = None


class TimerScript(BaseModel):
    arg: Optional[str] = None
    interval: Optional[int] = None
    script: Optional[str] = None


class TrapDest(BaseModel):
    IP: Optional[str] = None
    port: Optional[int] = None


class Triplet(BaseModel):
    device: Optional[str] = None
    mib: Optional[str] = None
    scenario: Optional[int] = None


class MimicAccessListGetResponse(RootModel[List[AccessEntry]]):
    root: List[AccessEntry]


class MimicAccessLoadFilenamePutResponse(RootModel[List[str]]):
    root: List[str]


class MimicAccessSaveFilenamePutResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumAddIPPostRequest(RootModel[List[Triplet]]):
    root: List[Triplet] = Field(..., description='Triplet array')


class MimicAgentAgentNumFromListGetResponse(RootModel[List[IPSource]]):
    root: List[IPSource]


class MimicAgentAgentNumGetMibsGetResponse(RootModel[List[Triplet]]):
    root: List[Triplet]


class MimicAgentAgentNumGetProtocolGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumIpaliasListGetResponse(RootModel[List[IPAlias]]):
    root: List[IPAlias]


class MimicAgentAgentNumProtocolMsgCoapGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgCoapGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgDhcpGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgDhcpGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgDhcpParamsGetResponse(
    RootModel[List[Dict[str, Any]]]
):
    root: List[Dict[str, Any]]


class MimicAgentAgentNumProtocolMsgIpmiGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgIpmiGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientGetProtstateGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientGetStateGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientMessageCardGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientMessageGetMsgNumAttrGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientMessageSetMsgNumAttrValuePutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientRuntimeAbortPutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientRuntimeConnectPutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientRuntimeDisconnectPutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientSetBrokerBrokerAddrPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetCleansessionCleanOrNotPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetClientidClientIDPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetKeepaliveAliveTimePutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetOnDisconnectActionPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetPasswordPasswordPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetPortPortPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetUsernameUsernamePutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetWillmsgMsgPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetWillqosQosPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetWillretainRetainPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSetWilltopicTopicPutResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSubscribeCardGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgMqttClientSubscribeGetSubNumAttrGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttClientSubscribeSetSubNumAttrValuePutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgMqttGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgMqttGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgNetflowFlowListGetResponse(
    RootModel[List[Dict[str, Any]]]
):
    root: List[Dict[str, Any]]


class MimicAgentAgentNumProtocolMsgNetflowGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgNetflowGetStatisticsGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgProxyGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgProxyGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgProxyPortListGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgSflowGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgSflowGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgSnmptcpGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgSnmptcpGetStatisticsGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgSnmptcpIpaliasListGetResponse(
    RootModel[List[IPAlias]]
):
    root: List[IPAlias]


class MimicAgentAgentNumProtocolMsgSnmpv3AccessListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3GroupListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3UserListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3UsmSavePutResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3UsmSaveasFilenamePutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3VacmSavePutResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3VacmSaveasFilenamePutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSnmpv3ViewListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolMsgSshGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgSshGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgSshIpaliasListGetResponse(RootModel[List[IPAlias]]):
    root: List[IPAlias]


class MimicAgentAgentNumProtocolMsgSyslogGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgSyslogGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTelnetConnectionLogonConnectionIDUserPasswordPutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetConnectionRequestConnectionIDCommandPutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetConnectionSignalConnectionIDSignalNamePutResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgTelnetGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTelnetIpaliasListGetResponse(
    RootModel[List[IPAlias]]
):
    root: List[IPAlias]


class MimicAgentAgentNumProtocolMsgTelnetServerGetConnectionsGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTelnetServerGetKeymapGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetServerGetRulesdbGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetServerGetStateGetResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTelnetServerGetUserdbGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgTelnetServerGetUsersGetResponse(
    RootModel[List[TelnetUser]]
):
    root: List[TelnetUser]


class MimicAgentAgentNumProtocolMsgTftpGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgTftpGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTftpSessionReadServerSrcfilePostResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTftpSessionWriteServerSrcfilePostResponse(
    RootModel[List[int]]
):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTodGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgTodGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgTodGettimeServerServerAddrPortPortNumScriptScriptNameTimeoutTimeSecRetriesNumRetriesGetResponse(
    RootModel[List[str]]
):
    root: List[str]


class MimicAgentAgentNumProtocolMsgWebGetArgsGetResponse(BaseModel):
    pass


class MimicAgentAgentNumProtocolMsgWebGetStatisticsGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumProtocolMsgWebPortExistsPortGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumProtocolProtGetConfigGetResponse(BaseModel):
    pass


class MimicAgentAgentNumSetMibsPutRequest(RootModel[List[Triplet]]):
    root: List[Triplet] = Field(..., description='Triplet array')


class MimicAgentAgentNumSetProtocolPutRequest(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumSetProtocolPutResponse(RootModel[List[int]]):
    root: List[int]


class MimicAgentAgentNumStoreListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumTimerScriptListGetResponse(RootModel[List[TimerScript]]):
    root: List[TimerScript]


class MimicAgentAgentNumTrapConfigListGetResponse(RootModel[List[TrapDest]]):
    root: List[TrapDest]


class MimicAgentAgentNumTrapListGetResponse(RootModel[List[str]]):
    root: List[str] = Field(..., description='array of OID or Object strings')


class MimicAgentAgentNumValueInstancesObjectGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumValueListOIDGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumValueMevalObjInsArrayGetResponse(RootModel[List[str]]):
    root: List[str]


class ObjInsArray(RootModel[List[List[str]]]):
    root: List[List[str]]


class MimicAgentAgentNumValueMgetObjInsVarArrayGetResponse(RootModel[List[str]]):
    root: List[str]


class ObjInsVarArray(RootModel[List[List[str]]]):
    root: List[List[str]]


class MimicAgentAgentNumValueMsetPutRequest(RootModel[List[List[str]]]):
    root: List[List[str]]


class MimicAgentAgentNumValueMunsetPutRequest(RootModel[List[List[str]]]):
    root: List[List[str]]


class MimicAgentAgentNumValueSplitOIDGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicAgentAgentNumValueVariablesObjectInstanceGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicClearFirstAgentNumLastAgentNumPutResponse(
    RootModel[Optional[Dict[str, int]]]
):
    root: Optional[Dict[str, int]] = None


class MimicGetActiveDataListGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicGetActiveListGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicGetCfgfileGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetCfgfileChangedGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetChangedConfigListGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicGetChangedStateListGetResponse(RootModel[List[AgentState]]):
    root: List[AgentState]


class MimicGetClientsGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetConfiguredListGetResponse(RootModel[List[int]]):
    root: List[int]


class MimicGetInterfacesGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetLogGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetNetaddrGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetNetdevGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetProductGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetProtocolsGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicGetReturnGetResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicLoadCfgFileFirstAgentNumLastAgentNumStartAgentNumPutResponse(
    RootModel[Optional[Dict[str, int]]]
):
    root: Optional[Dict[str, int]] = None


class MimicMgetInfoArrayGetResponse(RootModel[List[Dict[str, Any]]]):
    root: List[Dict[str, Any]]


class InfoArray(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgCoapGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgDhcpGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgIpmiGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgMqttGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgNetflowGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgProxyGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgSflowGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgSnmptcpGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgSshGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgSyslogGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgTelnetGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgTftpGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgTodGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicProtocolMsgWebGetStatsHdrGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicSavePutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicSaveasCfgFileFirstAgentNumLastAgentNumPutResponse(
    RootModel[Optional[Dict[str, int]]]
):
    root: Optional[Dict[str, int]] = None


class MimicSetNetdevPutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicSetPersistentPutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicStartPutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicStopPutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicStoreListGetResponse(RootModel[List[str]]):
    root: List[str]


class MimicTerminatePutResponse(RootModel[Optional[Dict[str, int]]]):
    root: Optional[Dict[str, int]] = None


class MimicTimerScriptListGetResponse(RootModel[List[TimerScript]]):
    root: List[TimerScript]
