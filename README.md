##### FASTAPI - POETRY - PYDANTIC - SQLALCHEMY - JINJA2 - TAILWINDCSS - SQLITE

# FastAPI Microservice boilerplate

This is an opinionated boilerplate to help bootstrap complex, large scale ML endpoints (or any kind of multiroute project).

### Features

- `fastapi.APIRouter` External Routing pattern `src/api/routes`
- `Poetry` for dependency management
- `Poetry run dev` development and build scripts
- `Pydantic` for data modelling
- `sqlalchemy` for schema modelling (ORM) and crud.
- `sqlite` database
- `src/api/static` static file serving (images)
- `jinja2` templates for html file service (homepage)
- `tailwindcss` for template styling

Roadmap:

- `bentoml` for model serving
- `mlflow` for model devops
- `az` azure ml studio for end point deployment

---

### How to use

#### 1. Clone

```zsh
git clone https://github.com/sinhaGuild/fastapi-poetry-boilerplate.git && cd fastapi-poetry-boilerplate
```

#### 2. Installing dependencies

```sh
poetry add `cat requirements.txt`
```

#### 3. Running the server

```sh
poetry run dev
```

#### 4. Navigate

##### `Home` - \

##### `Swagger` - \docs

##### `Redoc` - \redoc
