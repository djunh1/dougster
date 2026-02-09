from mangum import Mangum
from server import app

# Lambda handler
handler = Mangum(app)