model GENROU_70393a02 "annotation ()"
	OpenIPSL.Interfaces.PwPin plantaPin "something here" annotation ();
	OpenIPSL.Electrical.Machines.PSSE.GENROU sm_3_G3 (S_b=100,M_b=300,V_b=13.8,V_0=14.11809,angle_0=18.3354,P_0=-84.892,Q_0=12.455,R_a=0,Xl=0.1536,H=2.35,D=0.47,S10=1.01,S12=1.02,Tpd0=5.89,Tpq0=0.6,Tppd0=0.05,Tppq0=0.05,Xd=1.68,Xpd=0.2321,Xppd=0.21,Xq=1.61,Xpq=0.32,Xppq=0) "something here" annotation ();
equation
	connect(sm_3_G3.EFD0, sm_3_G3.EFD);
	connect(sm_3_G3.PMECH0, sm_3_G3.PMECH);
	connect(sm_3_G3.p, plantaPin);
end GENROU_70393a02;