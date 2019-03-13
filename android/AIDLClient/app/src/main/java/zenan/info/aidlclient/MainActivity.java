package zenan.info.aidlclient;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.zenan.aidl.IMyAidlInterface;

public class MainActivity extends AppCompatActivity {
    private IMyAidlInterface iMyAidlInterface;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        Intent intent = new Intent();
        intent.setPackage("com.zenan.aidl");
        intent.setAction("com.zenan.aidl.ibinder.action");

        bindService(intent, new ServiceConnection()
        {

            @Override
            public void onServiceConnected(ComponentName name, IBinder service)
            {

                iMyAidlInterface = IMyAidlInterface.Stub.asInterface(service);
                try {
                    Log.d("TAG", iMyAidlInterface.getName());
                } catch (RemoteException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onServiceDisconnected(ComponentName name)
            {

            }
        }, BIND_AUTO_CREATE);
    }
}
