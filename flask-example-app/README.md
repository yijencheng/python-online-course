# flask-example-app

A minimal flask-app that provide CORS api.
Example:
```

fetch(endpoint,{
    headers: {
        'Content-Type': 'application/json',
    },
    method: "POST",
    body: JSON.stringify(payload)
    })
.then(res=>res.json())
.then(data=>console.log(data))

```

