OPENQASM 2.0;
include "qelib1.inc";
gate r(param0,param1) q0 { u3(0.914521256031352,0,0) q0; }
gate r_47809095490000(param0,param1) q0 { u3(0.209462015758569,0,0) q0; }
gate r_47809095490816(param0,param1) q0 { u3(0.668736215747669,0,0) q0; }
gate r_47809095490960(param0,param1) q0 { u3(0.881366463037963,0,0) q0; }
gate r_47809095491392(param0,param1) q0 { u3(0.428922889973579,0,0) q0; }
gate r_47809095491536(param0,param1) q0 { u3(0.326108979863867,0,0) q0; }
gate r_47809071550864(param0,param1) q0 { u3(0.514482110445183,0,0) q0; }
gate r_47809071551056(param0,param1) q0 { u3(0.696041893153368,0,0) q0; }
gate r_47809095427552(param0,param1) q0 { u3(0.564040632726962,0,0) q0; }
gate r_47809095427264(param0,param1) q0 { u3(0.823949406610698,0,0) q0; }
gate r_47809095489280(param0,param1) q0 { u3(0.703933666366275,0,0) q0; }
gate r_47809095488992(param0,param1) q0 { u3(0.159158874698807,0,0) q0; }
gate r_47809095488416(param0,param1) q0 { u3(0.253564518268644,0,0) q0; }
gate r_47809095487984(param0,param1) q0 { u3(0.461720494645449,0,0) q0; }
gate r_47809067390432(param0,param1) q0 { u3(0.619275744096639,0,0) q0; }
gate r_47809067389568(param0,param1) q0 { u3(0.669802311727533,0,0) q0; }
gate r_47809067391248(param0,param1) q0 { u3(0.551577057174375,0,0) q0; }
gate r_47809067391920(param0,param1) q0 { u3(0.206936882815141,0,0) q0; }
qreg q[4];
u2(0,pi) q[0];
u(0,0,0) q[0];
u2(0,pi) q[0];
u(0,0,0) q[0];
u2(0,pi) q[1];
u(0,0,0) q[1];
u2(0,pi) q[1];
u(0,0,0) q[1];
u1(-pi/2) q[1];
cx q[1],q[0];
u1(0.435766599101355) q[0];
r(0.914521256031352,pi/2) q[1];
cx q[0],q[1];
r_47809095490000(0.209462015758569,pi/2) q[1];
cx q[1],q[0];
u1(pi/2) q[0];
u2(0,pi) q[2];
u(0,0,0) q[2];
u2(0,pi) q[2];
u(0,0,0) q[2];
u2(0,pi) q[3];
u(0,0,0) q[3];
u2(0,pi) q[3];
u(0,0,0) q[3];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[3];
cx q[3],q[2];
u1(0.46009795940112) q[2];
r_47809095490816(0.668736215747669,pi/2) q[3];
cx q[2],q[3];
r_47809095490960(0.881366463037963,pi/2) q[3];
cx q[3],q[2];
u1(pi/2) q[2];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[2];
cx q[2],q[1];
u1(0.396767606110413) q[1];
r_47809095491392(0.428922889973579,pi/2) q[2];
cx q[1],q[2];
r_47809095491536(0.326108979863867,pi/2) q[2];
cx q[2],q[1];
u1(pi/2) q[1];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[0];
cx q[0],q[3];
r_47809071550864(0.514482110445183,pi/2) q[0];
u1(0.128369743814755) q[3];
cx q[3],q[0];
r_47809071551056(0.696041893153368,pi/2) q[0];
cx q[0],q[3];
u1(pi/2) q[3];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[2];
cx q[2],q[0];
u1(0.746744205297659) q[0];
r_47809095427552(0.564040632726962,pi/2) q[2];
cx q[0],q[2];
r_47809095427264(0.823949406610698,pi/2) q[2];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[3];
cx q[3],q[1];
u1(0.657965996035714) q[1];
r_47809095489280(0.703933666366275,pi/2) q[3];
cx q[1],q[3];
r_47809095488992(0.159158874698807,pi/2) q[3];
barrier q[0],q[1],q[2],q[3];
u1(-pi/2) q[3];
cx q[3],q[2];
u1(0.117574535249454) q[2];
r_47809095488416(0.253564518268644,pi/2) q[3];
cx q[2],q[3];
r_47809095487984(0.461720494645449,pi/2) q[3];
cx q[3],q[2];
u1(pi/2) q[2];
barrier q[2],q[3];
u1(-pi/2) q[2];
cx q[2],q[3];
r_47809067390432(0.619275744096639,pi/2) q[2];
u1(0.363840439478916) q[3];
cx q[3],q[2];
r_47809067389568(0.669802311727533,pi/2) q[2];
cx q[2],q[3];
u1(pi/2) q[3];
barrier q[2],q[3];
u1(-pi/2) q[3];
cx q[3],q[2];
u1(0.771802747065588) q[2];
r_47809067391248(0.551577057174375,pi/2) q[3];
cx q[2],q[3];
r_47809067391920(0.206936882815141,pi/2) q[3];
barrier q[2],q[3];