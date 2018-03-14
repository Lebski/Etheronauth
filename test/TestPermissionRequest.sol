pragma solidity ^0.4.19;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Authority.sol";


contract TestPermissionRequest {
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

    function testOwnerUsingDeployedContract() public {
        Authority authContract = new Authority();

        address expected = address(this);

        Assert.equal(authContract.owner(), expected, "Owner not set correctly");
    }

    function testSuccessfullRequesting() public {
        Authority authContract = new Authority();
        //Authority authContract = Authority(DeployedAddresses.Authority());
        bytes32 _permissionId = 0x0000;

        addRequest(authContract, _permissionId);
        readRequest(authContract, _permissionId);
    }

    function addRequest (Authority authContract, bytes32 _permissionId) private {
        bytes32 _alg = "RS512";
        bytes32 _typ = "JWT";
        address _iss = "Tester";
        uint _sub = 1234567890;
        uint _audience = 1234567890;
        uint _exp = 1516239023;
        uint _nbf = 1516239022;
        uint _iat = 1516239022;

        authContract.addPermissionRequest(_permissionId, _alg, _typ, _iss, _sub, _audience, _exp, _nbf, _iat);
    }

    function readRequest (Authority authContract, bytes32 _permissionId) private {
        bytes32 alg = authContract.getRequestAlg(_permissionId);
        /*bytes32 typ = getRequestTyp(_permissionId);
        bytes32 iss = getRequestIss(_permissionId);
        uint sub = getRequestSub(_permissionId):
        uint audience =getRequestAud(_permissionId);
        uint exp = getRequestExp(_permissionId);
        uint nbf = getRequestNbf(_permissionId);
        uint iat = getRequestIat(_permissionId);*/
        uint jti = getRequestJti(_permissionId);

        //"Stack to deep"
        //(alg, typ, iss, sub, audience, exp, nbf, iat, jti) = authContract.getRequest(_permissionId);

        Assert.equal(alg, "RS512", "Alg ist not correctly set");
        Assert.equal(jti, "0", "Alg ist not correctly set");
    }

}
