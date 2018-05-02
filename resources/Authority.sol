pragma solidity ^0.4.17;


contract Authority {
    struct Levelobj {
        uint write;
        uint read;
    }

    struct Permissionrequest {
        bytes32 alg;
        bytes32 typ;
        address iss;
        address verifier;
        uint sub;
        uint audience;
        uint exp;
        uint nbf;
        uint iat;
        uint jti;
        bytes signature;
    }

    address public owner;
    uint private jtiCounter;
    mapping (address => mapping (bytes32 => uint)) public permissions; //addr zeigt auf ein obj, obj zeigt auf perm
    mapping (bytes32 => Permissionrequest) public permissionList;
    mapping (address => bool) public verifiers;

    event PermissionRequestDeployed (bytes32 permissionId);
    event PermissionGranted (bytes32 permissionId);

    // TODO: Change to 1 for release
    modifier validVerifiers(address _verifier) {
        require(verifiers[_verifier] == false);
        _;
    }

    modifier restricted() {
        if (msg.sender == owner) _;
    }

    function Authority() public {
        owner = msg.sender;
        jtiCounter = 0;
    }

    function addPermissionRequest (
        bytes32 _permissionId,
        bytes32 _alg,
        bytes32 _typ,
        uint _sub,
        uint _audience,
        uint _exp,
        uint _nbf,
        uint _iat) public {
        permissionList[_permissionId] = Permissionrequest(
        _alg, _typ, msg.sender, 0x0, _sub, _audience, _exp, _nbf, _iat, jtiCounter++, "0");
        PermissionRequestDeployed(_permissionId);
    }

    function storeSignature(bytes32 _permissionId, bytes _signature) public validVerifiers(msg.sender) {
        permissionList[_permissionId].signature = _signature;
        permissionList[_permissionId].verifier = msg.sender;
        PermissionGranted(_permissionId);
    }

    function setPermission(address _user, bytes32 _dataObject, uint _permissionLevel) public restricted {
        permissions[_user][_dataObject] = _permissionLevel;
    }

    /*
    * DOESNT WORK BECAUSE "Stack is too deep". Reuse this if future decisions
    * are made to reduce the var count
    function getRequest(bytes32 _permissionId) public view returns(
        bytes32 alg, bytes32 typ, bytes32 iss, uint sub, uint audience, uint exp, uint nbf, uint iat, uint jti) {
        Permissionrequest storage request = permissionList[_permissionId];
        return (request.alg, request.typ, request.iss, request.sub,
        request.audience, request.exp, request.nbf, request.iat, request.jti);
    }
    */
    function getRequestAlg(bytes32 _permissionId) public view returns(bytes32) {
        return permissionList[_permissionId].alg;
    }

    function getRequestTyp(bytes32 _permissionId) public view returns(bytes32) {
        return permissionList[_permissionId].typ;
    }

    function getRequestIss(bytes32 _permissionId) public view returns(address) {
        return permissionList[_permissionId].iss;
    }

    function getRequestSub(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].sub;
    }

    function getRequestAud(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].audience;
    }

    function getRequestExp(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].exp;
    }

    function getRequestNbf(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].nbf;
    }

    function getRequestIat(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].iat;
    }

    function getRequestJti(bytes32 _permissionId) public view returns(uint) {
        return permissionList[_permissionId].jti;
    }

    function getRequestSignature(bytes32 _permissionId) public view returns(bytes) {
        return permissionList[_permissionId].signature;
    }

    function getRequestVerifier(bytes32 _permissionId) public view returns(address) {
        return permissionList[_permissionId].verifier;
    }
}
