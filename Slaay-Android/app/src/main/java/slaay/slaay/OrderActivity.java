package slaay.slaay;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.error.VolleyError;
import com.android.volley.request.JsonObjectRequest;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class OrderActivity extends AppCompatActivity {

    private EditText creditNumber,expiration,amount;
    Button submitButton;
    String credit, price, expire;
    String merchantId="001";
    private String URL="http://35.196.16.101:8080/payment";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order);

        creditNumber=(EditText)findViewById(R.id.creditcard);
        expiration=(EditText)findViewById(R.id.expiration);
        amount=(EditText)findViewById(R.id.amount);
        submitButton=(Button)findViewById(R.id.submit);
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                credit = creditNumber.getText().toString();
                price = expiration.getText().toString();
                expire = amount.getText().toString();
                post();
            }
        });
    }

    public void post()
    {
        Map<String ,String > params = new HashMap<String, String>();
//        params.put("creditCard",credit);
//        params.put("amount",price);
//        params.put("expirationDate",expire);
//        params.put("merchantId",merchantId);

        //Log.e(TAG,"Params = " + params + " url = " + url);

        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.POST, URL, new JSONObject(params),
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        //hideProgressDialog();
                        //Log.e(TAG,"Response = " + response);
                        try {
                            Log.d("response", String.valueOf(response));
                            String token =  response.getString("transaction");

                            Toast.makeText(getApplicationContext(), token, Toast.LENGTH_LONG).show();

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
               // hideProgressDialog();
               // Toast.makeText(RegisterActivity.this,R.string.error,Toast.LENGTH_SHORT).show();
                //Log.e(TAG,"Error = " + error);
            }
        });
        MyApplication.getInstance().addToRequestQueue(jsonObjectRequest);
    }
}
