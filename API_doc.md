## Journal

### Create a Journal Entry

**Endpoint:** `/journal`  
**Method:** `POST`  
**Body:**

```json
{
    "title": "My Journal",
    "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
    "student_id": "661a53cd704ab3e24c34c1f0"
}
```
**Response:**
```json
{
    {
    "_id": "661a6b4dc3a6ec18e39e4284",
    "title": "My Journal",
    "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
    "student_id": "661a53cd704ab3e24c34c1f0",
    "sentiment_score": [
        {
        "label": "admiration",
        "score": 0.0018832245841622353
        },
        {
        "label": "amusement",
        "score": 0.00014939295942895114
        },
        {
        "label": "anger",
        "score": 0.000043181866203667596
        },
        {
        "label": "annoyance",
        "score": 0.0001045084572979249
        },
        {
        "label": "approval",
        "score": 0.005469656083732843
        },
        {
        "label": "caring",
        "score": 0.0015929717337712646
        },
        {
        "label": "confusion",
        "score": 0.00006960913742659613
        },
        {
        "label": "curiosity",
        "score": 0.0020051170140504837
        },
        {
        "label": "desire",
        "score": 0.0009177026804536581
        },
        {
        "label": "disappointment",
        "score": 0.00004128227010369301
        },
        {
        "label": "disapproval",
        "score": 0.00004420716504682787
        },
        {
        "label": "disgust",
        "score": 0.00009399560076417401
        },
        {
        "label": "embarrassment",
        "score": 0.00003549828761606477
        },
        {
        "label": "excitement",
        "score": 0.9622713327407837
        },
        {
        "label": "fear",
        "score": 0.0001684738090261817
        },
        {
        "label": "gratitude",
        "score": 0.0007345539052039385
        },
        {
        "label": "grief",
        "score": 0.000017212867533089593
        },
        {
        "label": "joy",
        "score": 0.020372958853840828
        },
        {
        "label": "love",
        "score": 0.00010325326002202928
        },
        {
        "label": "nervousness",
        "score": 0.00040247166180051863
        },
        {
        "label": "optimism",
        "score": 0.002253508660942316
        },
        {
        "label": "pride",
        "score": 0.00008751407585805282
        },
        {
        "label": "realization",
        "score": 0.00013485476665664464
        },
        {
        "label": "relief",
        "score": 0.00031680407118983567
        },
        {
        "label": "remorse",
        "score": 0.00006556484004249796
        },
        {
        "label": "sadness",
        "score": 0.000029908154829172418
        },
        {
        "label": "surprise",
        "score": 0.00036432879278436303
        },
        {
        "label": "neutral",
        "score": 0.000226801450480707
        }
    ],
    "created_at": "2024-04-13T11:23:57.520000",
    "updated_at": "2024-04-13T11:23:57.520000"
    }
}
```


### Get all Journal Entries
**Endpoint:** `/journal`  
**Method:** `GET`  
**Body:**

```json
{
    "title": "My Journal",
    "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
    "student_id": "661a53cd704ab3e24c34c1f0"
}
```
**Response:**
```json
[
    {
  "_id": "661a6b4dc3a6ec18e39e4284",
  "title": "My Journal",
  "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
  "student_id": "661a53cd704ab3e24c34c1f0",
  "sentiment_score": [
    {
      "label": "admiration",
      "score": 0.0018832245841622353
    },
    {
      "label": "amusement",
      "score": 0.00014939295942895114
    },
    {
      "label": "anger",
      "score": 0.000043181866203667596
    },
    {
      "label": "annoyance",
      "score": 0.0001045084572979249
    },
    {
      "label": "approval",
      "score": 0.005469656083732843
    },
    {
      "label": "caring",
      "score": 0.0015929717337712646
    },
    {
      "label": "confusion",
      "score": 0.00006960913742659613
    },
    {
      "label": "curiosity",
      "score": 0.0020051170140504837
    },
    {
      "label": "desire",
      "score": 0.0009177026804536581
    },
    {
      "label": "disappointment",
      "score": 0.00004128227010369301
    },
    {
      "label": "disapproval",
      "score": 0.00004420716504682787
    },
    {
      "label": "disgust",
      "score": 0.00009399560076417401
    },
    {
      "label": "embarrassment",
      "score": 0.00003549828761606477
    },
    {
      "label": "excitement",
      "score": 0.9622713327407837
    },
    {
      "label": "fear",
      "score": 0.0001684738090261817
    },
    {
      "label": "gratitude",
      "score": 0.0007345539052039385
    },
    {
      "label": "grief",
      "score": 0.000017212867533089593
    },
    {
      "label": "joy",
      "score": 0.020372958853840828
    },
    {
      "label": "love",
      "score": 0.00010325326002202928
    },
    {
      "label": "nervousness",
      "score": 0.00040247166180051863
    },
    {
      "label": "optimism",
      "score": 0.002253508660942316
    },
    {
      "label": "pride",
      "score": 0.00008751407585805282
    },
    {
      "label": "realization",
      "score": 0.00013485476665664464
    },
    {
      "label": "relief",
      "score": 0.00031680407118983567
    },
    {
      "label": "remorse",
      "score": 0.00006556484004249796
    },
    {
      "label": "sadness",
      "score": 0.000029908154829172418
    },
    {
      "label": "surprise",
      "score": 0.00036432879278436303
    },
    {
      "label": "neutral",
      "score": 0.000226801450480707
    }
  ],
  "created_at": "2024-04-13T11:23:57.520000",
  "updated_at": "2024-04-13T11:23:57.520000"

    },
]
```


### Get all Journal Entries by Student Id
**Endpoint:** `/journal/student/:studentid`  
**Method:** `GET`  
**Response:**
```json
[
    {
  "_id": "661a6b4dc3a6ec18e39e4284",
  "title": "My Journal",
  "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
  "student_id": "661a53cd704ab3e24c34c1f0",
  "sentiment_score": [
    {
      "label": "admiration",
      "score": 0.0018832245841622353
    },
    {
      "label": "amusement",
      "score": 0.00014939295942895114
    },
    {
      "label": "anger",
      "score": 0.000043181866203667596
    },
    {
      "label": "annoyance",
      "score": 0.0001045084572979249
    },
    {
      "label": "approval",
      "score": 0.005469656083732843
    },
    {
      "label": "caring",
      "score": 0.0015929717337712646
    },
    {
      "label": "confusion",
      "score": 0.00006960913742659613
    },
    {
      "label": "curiosity",
      "score": 0.0020051170140504837
    },
    {
      "label": "desire",
      "score": 0.0009177026804536581
    },
    {
      "label": "disappointment",
      "score": 0.00004128227010369301
    },
    {
      "label": "disapproval",
      "score": 0.00004420716504682787
    },
    {
      "label": "disgust",
      "score": 0.00009399560076417401
    },
    {
      "label": "embarrassment",
      "score": 0.00003549828761606477
    },
    {
      "label": "excitement",
      "score": 0.9622713327407837
    },
    {
      "label": "fear",
      "score": 0.0001684738090261817
    },
    {
      "label": "gratitude",
      "score": 0.0007345539052039385
    },
    {
      "label": "grief",
      "score": 0.000017212867533089593
    },
    {
      "label": "joy",
      "score": 0.020372958853840828
    },
    {
      "label": "love",
      "score": 0.00010325326002202928
    },
    {
      "label": "nervousness",
      "score": 0.00040247166180051863
    },
    {
      "label": "optimism",
      "score": 0.002253508660942316
    },
    {
      "label": "pride",
      "score": 0.00008751407585805282
    },
    {
      "label": "realization",
      "score": 0.00013485476665664464
    },
    {
      "label": "relief",
      "score": 0.00031680407118983567
    },
    {
      "label": "remorse",
      "score": 0.00006556484004249796
    },
    {
      "label": "sadness",
      "score": 0.000029908154829172418
    },
    {
      "label": "surprise",
      "score": 0.00036432879278436303
    },
    {
      "label": "neutral",
      "score": 0.000226801450480707
    }
  ],
  "created_at": "2024-04-13T11:23:57.520000",
  "updated_at": "2024-04-13T11:23:57.520000"

    },
]
```

### Get Journal Entry by Id
**Endpoint:** `/journal/:studentid`  
**Method:** `GET`  
**Response:**
```json

    {
  "_id": "661a6b4dc3a6ec18e39e4284",
  "title": "My Journal",
  "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
  "student_id": "661a53cd704ab3e24c34c1f0",
  "sentiment_score": [
    {
      "label": "admiration",
      "score": 0.0018832245841622353
    },
    {
      "label": "amusement",
      "score": 0.00014939295942895114
    },
    {
      "label": "anger",
      "score": 0.000043181866203667596
    },
    {
      "label": "annoyance",
      "score": 0.0001045084572979249
    },
    {
      "label": "approval",
      "score": 0.005469656083732843
    },
    {
      "label": "caring",
      "score": 0.0015929717337712646
    },
    {
      "label": "confusion",
      "score": 0.00006960913742659613
    },
    {
      "label": "curiosity",
      "score": 0.0020051170140504837
    },
    {
      "label": "desire",
      "score": 0.0009177026804536581
    },
    {
      "label": "disappointment",
      "score": 0.00004128227010369301
    },
    {
      "label": "disapproval",
      "score": 0.00004420716504682787
    },
    {
      "label": "disgust",
      "score": 0.00009399560076417401
    },
    {
      "label": "embarrassment",
      "score": 0.00003549828761606477
    },
    {
      "label": "excitement",
      "score": 0.9622713327407837
    },
    {
      "label": "fear",
      "score": 0.0001684738090261817
    },
    {
      "label": "gratitude",
      "score": 0.0007345539052039385
    },
    {
      "label": "grief",
      "score": 0.000017212867533089593
    },
    {
      "label": "joy",
      "score": 0.020372958853840828
    },
    {
      "label": "love",
      "score": 0.00010325326002202928
    },
    {
      "label": "nervousness",
      "score": 0.00040247166180051863
    },
    {
      "label": "optimism",
      "score": 0.002253508660942316
    },
    {
      "label": "pride",
      "score": 0.00008751407585805282
    },
    {
      "label": "realization",
      "score": 0.00013485476665664464
    },
    {
      "label": "relief",
      "score": 0.00031680407118983567
    },
    {
      "label": "remorse",
      "score": 0.00006556484004249796
    },
    {
      "label": "sadness",
      "score": 0.000029908154829172418
    },
    {
      "label": "surprise",
      "score": 0.00036432879278436303
    },
    {
      "label": "neutral",
      "score": 0.000226801450480707
    }
  ],
  "created_at": "2024-04-13T11:23:57.520000",
  "updated_at": "2024-04-13T11:23:57.520000"

    },
```




### Update a Journal Entriy
**Endpoint:** `/journal/:id`  
**Method:** `PATCH`  
**Body:**

```json
{
    "title": "My Journal",
    "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
}
```
**Response:**
```json
    {
  "_id": "661a6b4dc3a6ec18e39e4284",
  "title": "My Journal",
  "entry": "This is my journal entry. Today was a good day. I learned a lot in my classes and I'm excited for what's to come. I'm feeling positive and motivated to continue working hard.",
  "student_id": "661a53cd704ab3e24c34c1f0",
  "sentiment_score": [
    {
      "label": "admiration",
      "score": 0.0018832245841622353
    },
    {
      "label": "amusement",
      "score": 0.00014939295942895114
    },
    {
      "label": "anger",
      "score": 0.000043181866203667596
    },
    {
      "label": "annoyance",
      "score": 0.0001045084572979249
    },
    {
      "label": "approval",
      "score": 0.005469656083732843
    },
    {
      "label": "caring",
      "score": 0.0015929717337712646
    },
    {
      "label": "confusion",
      "score": 0.00006960913742659613
    },
    {
      "label": "curiosity",
      "score": 0.0020051170140504837
    },
    {
      "label": "desire",
      "score": 0.0009177026804536581
    },
    {
      "label": "disappointment",
      "score": 0.00004128227010369301
    },
    {
      "label": "disapproval",
      "score": 0.00004420716504682787
    },
    {
      "label": "disgust",
      "score": 0.00009399560076417401
    },
    {
      "label": "embarrassment",
      "score": 0.00003549828761606477
    },
    {
      "label": "excitement",
      "score": 0.9622713327407837
    },
    {
      "label": "fear",
      "score": 0.0001684738090261817
    },
    {
      "label": "gratitude",
      "score": 0.0007345539052039385
    },
    {
      "label": "grief",
      "score": 0.000017212867533089593
    },
    {
      "label": "joy",
      "score": 0.020372958853840828
    },
    {
      "label": "love",
      "score": 0.00010325326002202928
    },
    {
      "label": "nervousness",
      "score": 0.00040247166180051863
    },
    {
      "label": "optimism",
      "score": 0.002253508660942316
    },
    {
      "label": "pride",
      "score": 0.00008751407585805282
    },
    {
      "label": "realization",
      "score": 0.00013485476665664464
    },
    {
      "label": "relief",
      "score": 0.00031680407118983567
    },
    {
      "label": "remorse",
      "score": 0.00006556484004249796
    },
    {
      "label": "sadness",
      "score": 0.000029908154829172418
    },
    {
      "label": "surprise",
      "score": 0.00036432879278436303
    },
    {
      "label": "neutral",
      "score": 0.000226801450480707
    }
  ],
  "created_at": "2024-04-13T11:23:57.520000",
  "updated_at": "2024-04-13T11:23:57.520000"

    },

```


### Delete a Journal Entry
**Endpoint:** `/journal/:id`  
**Method:** `Delete`  




## Student

### Register a Student

**Endpoint:** `/student/register`  
**Method:** `POST`  
**Body:**

```json
{
    "firstName": "John",
    "lastName": "Doe",
    "userName": "johndoe",
    "email": "john@school.com",
    "course_of_study": "Computer Science",
    "year": 2,
    "password": "password123"
}
```
**Response:**
```json
{
  "_id": "661a5930cfe4cceb3c4772a1",
  "firstName": "Abdulazeez",
  "lastName": "Abdulazeez Adeshina",
  "userName": "abdul",
  "email": "abdul@school.com",
  "course_of_study": "Water resources engineering",
  "year": 3,
  "password": "$2b$12$MG8/Xp30ZINVtMYB.DTGtOq2//x6kiUL6jTnhDK6Q9PaMEjJvsOiW"
}
```

### Login a Student

**Endpoint:** `student/login`  
**Method:** `POST`  
**Body:**

```json
{
    "email": "john@school.com",
    "password": "password123"
}
```
**Response:**
```json
{
  "detail": "Student successfully logged in",
  "student_id": "661a53cd704ab3e24c34c1f0"
}
```
**Error Response**
```json
{
    "detail": "Incorrect email or password"
}
```

### Get all students

**Endpoint:** `/student`  
**Method:** `GET`  
**Body:**

```json
{
    "firstName": "John",
    "lastName": "Doe",
    "userName": "johndoe",
    "email": "john@school.com",
    "course_of_study": "Computer Science",
    "year": 2,
    "password": "password123"
}
```
**Response:**
```json
{
  "_id": "60d5fbd7a3f8f2e167fe5775",
  "firstName": "John",
  "lastName": "Doe",
  "userName": "johndoe",
  "email": "john@school.com",
  "course_of_study": "Computer Science",
  "year": 2,
  "password": "$2b$12$KbQiHKTdjEvzvkBaJ0KZteG7E0/9aA7iS3YiDkPe/WzdETa5bHZHy"
}
```

### Get a student

**Endpoint:** `/student/:studentid`  
**Method:** `GET`  
**Response:**
```json
{
  "_id": "661a53cd704ab3e24c34c1f0",
  "firstName": "Ej",
  "lastName": "dee",
  "userName": "ejjjjj",
  "email": "ejdee@gmail.com",
  "course_of_study": "Water resources engineering",
  "year": 4,
  "password": "$2b$12$mZeH91NoQq3JZX13TJnJyeaQQG8XzUcZqYqFj.68OVoO7Iyn4IOUu"
}
```

## Admin


### Register a Admin

**Endpoint:** `/admin/register`  
**Method:** `POST`  
**Body:**

```json
{
  "email": "admin@admin.com",
  "firstName": "Admin",
  "lastName": "User",
  "password": "admin123"
}
```
**Response:**
```json
{
  "_id": "661a760aeb725fb0b95bde47",
  "firstName": "Admin",
  "lastName": "User",
  "email": "admin@admin.com",
  "password": "$2b$12$ozP6DlVP/oN7ZGCMc5aZ0.mw2PnpY3dGciM.gQF8ePG5ajKOMcDce"
}
```

### Login a Admin

**Endpoint:** `admin/login`  
**Method:** `POST`  
**Body:**

```json
{
  "email": "admin@admin.com",
  "password": "admin123"
}
```
**Response:**
```json
{
  "detail": "Admin successfully logged in",
  "admin_id": "661a760aeb725fb0b95bde47"
}
```
**Error Response**
```json
{
    "detail": "Incorrect email or password"
}
```


### Get a admin

**Endpoint:** `/admin/:adminid`  
**Method:** `GET`  
**Response:**
```json
{
  "_id": "661a760aeb725fb0b95bde47",
  "firstName": "Admin",
  "lastName": "User",
  "email": "admin@admin.com",
  "password": "$2b$12$ozP6DlVP/oN7ZGCMc5aZ0.mw2PnpY3dGciM.gQF8ePG5ajKOMcDce"
}
```

