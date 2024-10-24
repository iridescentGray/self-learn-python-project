import functools
import logging
import typing

import jenkins
import xmltodict

logger = logging.getLogger("JenkinsApi")


def retry(times: int = 3, exceptions=Exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    if attempt < times:
                        logging.error(
                            f"Exception thrown when attempting to run {func}, attempt {attempt} of {times}"
                        )
                    else:
                        logging.exception(
                            f"Exception thrown when attempting to run {func} after {times} attempts"
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorator


class JenkinsApi(object):
    def __init__(self, url: str, uname: str, passwd: str):
        self.jenkins_url: str = url
        self.jenkins_username: str = uname
        self.jenkins_password: str = passwd
        self._jenkins_server: typing.Optional[jenkins.Jenkins] = None

    @retry()
    def try_login_jenkins(self) -> jenkins.Jenkins:
        server = jenkins.Jenkins(
            self.jenkins_url, self.jenkins_username, self.jenkins_password
        )
        server.get_whoami()
        return server

    @property
    def jenkins_server(self) -> jenkins.Jenkins:
        if not self._jenkins_server:
            self._jenkins_server = self.try_login_jenkins()

        try:
            self._jenkins_server.get_whoami()
        except jenkins.JenkinsException as e:
            self._jenkins_server = self.try_login_jenkins()
            if not self._jenkins_server:
                raise e

        return self._jenkins_server

    def get_all_jobs(self) -> typing.Optional[list]:
        try:
            res = self.jenkins_server.get_jobs()
            return res
        except Exception as e:
            logger.error(f"get_all_jobs error,reason:{str(e)}")

    def get_all_view_info(self) -> typing.Any:
        try:
            res = self.jenkins_server.get_views()
            return res
        except Exception as e:
            logger.error(f"get_all_view_info error,reason:{str(e)}")

    def get_job_info(self, job_name: str) -> typing.Optional[dict]:
        try:
            res = self.jenkins_server.get_job_info(name=job_name)
            return res
        except Exception as e:
            logger.error(f"get_job_info error,reason:{str(e)}")

    def is_job_exists(self, job_name: str) -> bool:
        try:
            job_exists = self.jenkins_server.job_exists(name=job_name)
            if not job_exists:
                return False
            return True
        except Exception as e:
            logger.error(f"is_job_exists error,reason:{str(e)}")
            return False

    def get_job_conf(self, job_name: str) -> typing.Optional[dict]:
        try:
            res = self.jenkins_server.get_job_config(job_name)
            xml_parse = xmltodict.parse(res)
            return xml_parse
        except Exception as e:
            logger.error(f"get_job_conf error,reason:{str(e)}")

    def reconfig_job(self, job_name: str, job_config: dict) -> bool:
        config_xml = xmltodict.unparse(job_config)
        try:
            self.jenkins_server.reconfig_job(job_name, config_xml)
            return True
        except Exception as e:
            logger.error(f"reconfig_job error,reason:{str(e)}")
            return False

    def get_job_nextbuildnumber(self, job_name: str) -> typing.Optional[int]:
        try:
            job_info = self.get_job_info(job_name=job_name)
            if not job_info:
                return None
            return job_info["nextBuildNumber"]
        except Exception as e:
            logger.error(f"get_job_nextbuildnumber error,reason:{str(e)}")

    def get_job_lastbuildnumber(self, job_name: str) -> typing.Optional[int]:
        try:
            job_info = self.get_job_info(job_name=job_name)
            if not job_info:
                return None
            return job_info["lastBuild"]["number"]
        except Exception as e:
            logger.error(f"get_job_lastbuildnumber error,reason:{str(e)}")

    def get_job_build_status(
        self, job_name: str, build_number: int
    ) -> typing.Optional[int]:
        try:
            job_status = self.jenkins_server.get_build_info(
                name=job_name, number=build_number
            )["result"]
            return job_status
        except Exception as e:
            logger.error(f"get_job_build_status error,reason:{str(e)}")

    def start_job_build(self, job_name: str, parameters=None) -> typing.Optional[int]:
        try:
            res = self.jenkins_server.build_job(name=job_name, parameters=parameters)
            return res
        except Exception as e:
            logger.error(f"start_job_build error,reason:{str(e)}")

    def stop_job_build(self, job_name: str, build_number: int) -> typing.Optional[int]:
        try:
            res = self.jenkins_server.stop_build(name=job_name, number=build_number)
            return res
        except Exception as e:
            logger.error(f"stop_job_build error,reason:{str(e)}")

    def get_bulid_log(self, job_name: str, build_number: int) -> typing.Optional[str]:
        try:
            res = self.jenkins_server.get_build_console_output(
                name=job_name, number=build_number
            )
            return res
        except Exception as e:
            logger.error(f"get_bulid_log error,reason:{str(e)}")

    def get_all_view(self) -> typing.Optional[list]:
        try:
            res = self.jenkins_server.get_views()
            return res
        except Exception as e:
            logger.error(f"get_all_view error,reason:{str(e)}")

    def copy_job(self, source_job: str, target_job: str) -> bool:
        try:
            source_job_config_xml = self.jenkins_server.get_job_config(source_job)
            self.jenkins_server.create_job(target_job, source_job_config_xml)
            return True
        except Exception as e:
            logger.error(f"get_all_view error,reason:{str(e)}")
            return False
