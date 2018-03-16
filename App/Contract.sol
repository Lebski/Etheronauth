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
        uint sub;
        uint audience;
        uint exp;
        uint nbf;
        uint iat;
        uint jti;
        bytes signature;
    }

    address public owner;
    uint public lastCompletedMmigration;
    uint private jtiCounter;
    mapping (address => Levelobj) public permissions;
    mapping (bytes32 => Permissionrequest) public permissionList;

    event PermissionRequestdeployed (bytes32 permissionId);
    event PermissionGranted (bytes32 permissionId);

    modifier restricted() {
        if (msg.sender == owner) _;
    }

    function Authority() public {
        owner = msg.sender;
        jtiCounter = 0;
    }

    function addPermissionRequest (
        //sender ID
        bytes32 _permissionId,
        bytes32 _alg,
        bytes32 _typ,
        address _iss,
        uint _sub,
        uint _audience,
        uint _exp,
        uint _nbf,
        uint _iat) public {
        permissionList[_permissionId] = Permissionrequest(
        _alg, _typ, _iss, _sub, _audience, _exp, _nbf, _iat, jtiCounter++, "0");
        PermissionRequestdeployed(_permissionId);
    }

    function addPermissionRequest () public {
        jtiCounter = 0;
    }

    /*
    * DOESNT WORK BECAUSE "Stack is too deep"
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

}
