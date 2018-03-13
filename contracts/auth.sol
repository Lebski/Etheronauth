pragma solidity 0.4.21;


contract Authority {
    struct Levelobj {
        uint write;
        uint read;
    }

    struct Permissionrequest {
        bytes32 alg;
        bytes32 typ;
        bytes32 iss;
        uint sub;
        uint audience;
        uint exp;
        uint nbf;
        uint iat;
        uint jti;
    }

    address public owner;
    uint public lastCompletedMmigration;
    mapping (address => Levelobj) public permissions;
    mapping (bytes32 => Permissionrequest) public permissionList;

    modifier restricted() {
        if (msg.sender == owner) _;
    }

    function Authority() public {
        owner = msg.sender;
    }

    function addPermissionRequest(
        //sender ID
        bytes32 _permissionId,
        bytes32 _alg,
        bytes32 _typ,
        bytes32 _iss,
        uint _sub,
        uint _audience,
        uint _exp,
        uint _nbf,
        uint _iat,
        uint _jti) public {
        permissionList[_permissionId] = Permissionrequest(_alg, _typ, _iss, _sub, _audience, _exp, _nbf, _iat, _jti);
    }



}
