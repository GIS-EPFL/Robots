MODULE RapidCom
VAR bool RunTuneProc:=false;
PERS tooldata tuneTool :=[TRUE,[[0,0,0],[1,0,0,0]],[0.001,[0,0,0.001],[1,0,0,0],0,0,0]];

PROC LoadTuneProc()
VAR bool tuneProcLoaded:=false;
    WHILE tuneProcLoaded=false DO
        tuneProcLoaded:=true;
        Load \Dynamic,"TEMP:" \File:= "/tune.sys";
    ENDWHILE
ERROR
    tuneProcLoaded:=false;
    WaitTime 0.01;
    TRYNEXT;
ENDPROC

PROC TMMainProc()
    WHILE true DO
        IF RunTuneProc THEN
            LoadTuneProc;
            %"tuneproc"%;
            UnLoad "TEMP:" \File:= "/tune.sys";
            RunTuneProc:=false;
        ELSE
            WaitTime 0.01;
        ENDIF
    ENDWHILE
ENDPROC
ENDMODULE